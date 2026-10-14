#!/usr/bin/env python3
"""Notify IndexNow about changed public pages after a successful Pages deploy."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ENDPOINT = "https://api.indexnow.org/indexnow"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def validate_url(url, host):
    parts = urlsplit(url)
    if (parts.scheme != "https" or parts.netloc != host
            or parts.username or parts.password or parts.fragment or parts.query):
        raise ValueError("URL must be a canonical HTTPS URL on " + host + ": " + url)
    return url


def sitemap_urls(content, host):
    root = ET.fromstring(content)
    if root.tag != NS + "urlset":
        raise ValueError("Expected a sitemap urlset")
    urls = sorted({validate_url(node.text.strip(), host)
                   for node in root.findall(NS + "url/" + NS + "loc")})
    if not urls or len(urls) > 10000:
        raise ValueError("Expected between 1 and 10,000 sitemap URLs")
    return urls


def request(url, data=None):
    headers = {"User-Agent": "NicolasLescalier-IndexNow/1.0", "Cache-Control": "no-cache"}
    if data is not None:
        headers["Content-Type"] = "application/json; charset=utf-8"
    for attempt in range(4):
        try:
            with urlopen(Request(url, data=data, headers=headers), timeout=30) as response:
                return response.status, response.read(), response.headers, response.url
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise
        except (URLError, TimeoutError):
            if attempt == 3:
                raise
        time.sleep(2 ** (attempt + 1))


class PageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.noindex = False
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name", "").lower() in ("robots", "bingbot"):
            self.noindex |= bool(re.search(r"\b(noindex|none)\b", attrs.get("content", ""), re.I))
        if tag == "link" and "canonical" in attrs.get("rel", "").lower().split():
            self.canonical = attrs.get("href")


def page_fingerprint(url, host):
    status, content, headers, final_url = request(url)
    validate_url(final_url, host)
    if status != 200 or final_url != url:
        raise ValueError("Sitemap URL must return 200 without redirecting: " + url)
    if "text/html" not in headers.get("Content-Type", "").lower():
        raise ValueError("Expected HTML at " + url)
    page = PageMetadata()
    page.feed(content.decode("utf-8"))
    if page.canonical != url:
        raise ValueError("Sitemap URL has a missing or different canonical: " + url)
    header_noindex = re.search(r"\b(noindex|none)\b", headers.get("X-Robots-Tag", ""), re.I)
    if page.noindex or header_noindex:
        return url, None
    return url, hashlib.sha256(content).hexdigest()


def changed_urls(previous, current):
    # Previously indexed URLs that are removed or become noindex also need a recrawl.
    return sorted(url for url in previous.keys() | current.keys()
                  if previous.get(url) != current.get(url))


def submit(host, key, urls):
    payload = {"host": host, "key": key,
               "keyLocation": "https://" + host + "/" + key + ".txt", "urlList": urls}
    status, _, _, _ = request(ENDPOINT, json.dumps(payload).encode("utf-8"))
    if status not in (200, 202):
        raise RuntimeError("Unexpected IndexNow HTTP status: " + str(status))
    return status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--state", type=Path, default=Path(".indexnow-state/pages.json"))
    args = parser.parse_args()
    config = json.loads(Path(".github/indexnow.json").read_text())
    host, key = config["host"], config["key"]
    if host != "nicolaslescalier.com" or not re.fullmatch(r"[a-f0-9]{32}", key):
        raise ValueError("Invalid IndexNow configuration")
    if Path(key + ".txt").read_text().strip() != key:
        raise ValueError("Local ownership file does not match configuration")
    origin = "https://" + host
    # Dry runs can validate the site before the new ownership file is deployed.
    if not args.dry_run:
        _, content, _, final_url = request(origin + "/" + key + ".txt")
        if final_url != origin + "/" + key + ".txt" or content.decode("utf-8").strip() != key:
            raise ValueError("Live ownership file is missing or incorrect; nothing submitted")
    _, content, _, final_url = request(origin + "/sitemap.xml")
    if final_url != origin + "/sitemap.xml":
        raise ValueError("Unexpected sitemap redirect")
    urls = sitemap_urls(content, host)
    previous = json.loads(args.state.read_text()) if args.state.exists() else {}
    if not isinstance(previous, dict):
        raise ValueError("Invalid cached page state")
    for url, digest in previous.items():
        validate_url(url, host)
        if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
            raise ValueError("Invalid cached fingerprint")
    with ThreadPoolExecutor(max_workers=4) as pool:
        current = {url: digest for url, digest in pool.map(
            lambda url: page_fingerprint(url, host), urls) if digest is not None}
    changed = changed_urls(previous, current)
    if len(changed) > 10000:
        raise ValueError("Too many changed URLs for one IndexNow submission")
    print("Validated %d sitemap URLs; %d indexable; %d changed." % (len(urls), len(current), len(changed)))
    if args.dry_run:
        print("Dry run: no URLs submitted and no state saved.")
        return
    status = submit(host, key, changed) if changed else None
    if status == 202:
        message = "IndexNow accepted %d URLs; ownership validation is pending. State not saved." % len(changed)
    else:
        message = ("IndexNow received %d URLs (HTTP 200)." % len(changed) if changed
                   else "No changed URLs; no IndexNow request needed.")
        args.state.parent.mkdir(parents=True, exist_ok=True)
        args.state.write_text(json.dumps(current, sort_keys=True, indent=2) + "\n")
    print(message)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as output:
            output.write("## IndexNow\n\n" + message + "\n\nSubmission does not guarantee indexing or ranking.\n")
            if changed:
                output.write("\n" + "\n".join("- " + url for url in changed) + "\n")


if __name__ == "__main__":
    main()
