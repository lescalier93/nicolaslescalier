import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('check_site', Path(__file__).parents[1] / 'scripts/check_site.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
BASE = 'https://nicolaslescalier.com'


class SiteAuditTests(unittest.TestCase):
    def run_site(self, changes='', robots=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'robots.txt').write_text(robots or f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
            (root / 'sitemap.xml').write_text(f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc></url></urlset>')
            (root / 'index.html').write_text(f'''<!doctype html><title>Test page</title><meta name="description" content="Test description"><meta property="og:url" content="{BASE}/"><link rel="canonical" href="{BASE}/"><h1 id="top">Title</h1><a href="#top">Top</a><script type="application/ld+json">{{"@type":"WebPage"}}</script>{changes}''')
            return check.audit(root, BASE)[0]

    def test_valid_site_and_fragment_pass(self):
        self.assertEqual(self.run_site(), [])

    def test_noindex_and_duplicate_canonical_fail(self):
        errors = self.run_site('<meta name="robots" content="noindex"><link rel="canonical" href="https://other.example/">')
        self.assertTrue(any('restrictive robots' in e for e in errors))
        self.assertTrue(any('canonical' in e for e in errors))

    def test_missing_page_fragment_and_json_fail(self):
        errors = self.run_site('<a href="/missing/">Missing</a><a href="#missing">Fragment</a><script type="application/ld+json">{broken}</script>')
        self.assertTrue(any('broken internal link' in e for e in errors))
        self.assertTrue(any('missing link target' in e for e in errors))
        self.assertTrue(any('invalid JSON-LD' in e for e in errors))

    def test_specific_ai_crawler_block_fails(self):
        errors = self.run_site(robots=f'User-agent: OAI-SearchBot\nDisallow: /\n\nUser-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
        self.assertTrue(any('blocks OAI-SearchBot' in e for e in errors))
        self.assertFalse(any('blocks Googlebot' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
