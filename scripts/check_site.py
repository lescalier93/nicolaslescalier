"""Audit the built public sitemap and its pages before deployment (stdlib only)."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

CRAWLERS = ('Googlebot', 'bingbot', 'OAI-SearchBot', 'PerplexityBot',
            'Claude-SearchBot', 'DuckDuckBot', 'Applebot', 'Bravebot', 'Qwantbot')


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.titles = []
        self.meta = {}
        self.canonicals = []
        self.links = []
        self.images = []
        self.ids = set()
        self.h1 = 0
        self.jsonld = []
        self.in_title = False
        self.ld = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'title':
            self.in_title = True
            self.titles.append('')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta':
            key = a.get('name', a.get('property', '')).lower()
            self.meta[key] = a.get('content', '')
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonicals.append(a.get('href', ''))
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'img':
            self.images.append(a)
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.ld = []

    def handle_data(self, data):
        if self.in_title:
            self.titles[-1] += data
        if self.ld is not None:
            self.ld.append(data)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'script' and self.ld is not None:
            self.jsonld.append(''.join(self.ld))
            self.ld = None


def local_file(root, url):
    path = unquote(urlsplit(url).path).lstrip('/')
    file = (root / path).resolve()
    if not file.is_relative_to(root.resolve()):
        return None
    return file / 'index.html' if file.is_dir() or not Path(path).suffix else file


def audit(root, base):
    root = Path(root)
    base = base.rstrip('/')
    errors = []
    try:
        tree = ET.parse(root / 'sitemap.xml')
        urls = [e.text for e in tree.findall('{*}url/{*}loc')]
    except (OSError, ET.ParseError) as e:
        return [f'Invalid sitemap: {e}'], 0
    if not urls:
        errors.append('Sitemap contains no page URLs')
    if len(urls) != len(set(urls)):
        errors.append('Sitemap contains duplicate URLs')
    robots = RobotFileParser()
    try:
        robots_text = (root / 'robots.txt').read_text()
        robots.parse(robots_text.splitlines())
        if base + '/sitemap.xml' not in (robots.site_maps() or []):
            errors.append('robots.txt must advertise the canonical sitemap')
    except OSError:
        errors.append('Missing robots.txt')
        robots.parse([])

    pages = {}
    titles, descriptions = Counter(), Counter()
    incoming = set()
    for url in urls:
        if not url or urlsplit(url).scheme != 'https' or urlsplit(url).netloc != urlsplit(base).netloc:
            errors.append(f'Noncanonical sitemap origin: {url}')
            continue
        file = local_file(root, url)
        if not file or not file.is_file():
            errors.append(f'Missing sitemap page: {url}')
            continue
        page = Page(file.read_text())
        pages[url] = page
        if page.canonicals != [url]:
            errors.append(f'{url}: expected exactly one self-referencing canonical')
        if len(page.titles) != 1 or not page.titles[0].strip():
            errors.append(f'{url}: missing or duplicate title element')
        else:
            titles[page.titles[0].strip()] += 1
        description = page.meta.get('description', '').strip()
        if not description:
            errors.append(f'{url}: missing description')
        else:
            descriptions[description] += 1
        if page.h1 != 1:
            errors.append(f'{url}: expected one H1, found {page.h1}')
        if page.meta.get('og:url') != url:
            errors.append(f'{url}: social URL differs from canonical')
        for agent in CRAWLERS:
            if not robots.can_fetch(agent, url):
                errors.append(f'{url}: robots.txt blocks {agent}')
        for name, value in page.meta.items():
            if name in ('robots',) + tuple(a.lower() for a in CRAWLERS):
                if re.search(r'\b(noindex|none|nosnippet)\b|max-snippet\s*:\s*0\b', value, re.I):
                    errors.append(f'{url}: restrictive {name} directive: {value}')
        if not page.jsonld:
            errors.append(f'{url}: missing structured data')
        for value in page.jsonld:
            try:
                parsed = json.loads(value)
                if not isinstance(parsed, (dict, list)):
                    raise ValueError('Expected a JSON object or array')
            except ValueError as e:
                errors.append(f'{url}: invalid JSON-LD: {e}')
        for img in page.images:
            if 'alt' not in img or not img.get('width') or not img.get('height'):
                errors.append(f'{url}: image lacks alt or dimensions: {img.get("src")}')
            src = urljoin(url, img.get('src', ''))
            if urlsplit(src).netloc == urlsplit(base).netloc:
                target = local_file(root, src)
                if not target or not target.is_file():
                    errors.append(f'{url}: missing image: {src}')

    # Check internal navigation independently of the sitemap: thank-you pages and
    # redirects can be valid destinations without being indexable search pages.
    cache = {local_file(root, url): page for url, page in pages.items()}
    for url, page in pages.items():
        for href in page.links:
            target_url = urljoin(url, href)
            parts = urlsplit(target_url)
            if parts.scheme not in ('http', 'https') or parts.netloc != urlsplit(base).netloc:
                continue
            target = local_file(root, target_url)
            if not target or not target.is_file():
                errors.append(f'{url}: broken internal link: {href}')
                continue
            canonical_destination = parts._replace(query='', fragment='').geturl()
            if canonical_destination != url:
                incoming.add(canonical_destination)
            if parts.fragment and target.suffix == '.html':
                if target not in cache:
                    cache[target] = Page(target.read_text())
                if unquote(parts.fragment) not in cache[target].ids:
                    errors.append(f'{url}: missing link target: {href}')
    for url in urls:
        if url != base + '/' and url not in incoming:
            errors.append(f'{url}: no incoming link from another sitemap page')
    errors.extend(f'Duplicate title: {title}' for title, n in titles.items() if n > 1)
    errors.extend(f'Duplicate description: {desc}' for desc, n in descriptions.items() if n > 1)
    return sorted(set(errors)), len(pages)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--base', default='https://nicolaslescalier.com')
    args = parser.parse_args()
    issues, count = audit(args.site, args.base)
    for issue in issues:
        print('ERROR:', issue)
    print(f'Checked {count} sitemap pages; {len(issues)} issues.')
    raise SystemExit(bool(issues))
