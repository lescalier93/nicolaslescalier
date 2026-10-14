import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("indexnow", Path(__file__).parents[1] / "scripts/indexnow.py")
indexnow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(indexnow)
HOST = "nicolaslescalier.com"
URL = "https://" + HOST + "/"


class IndexNowTests(unittest.TestCase):
    def test_sitemap_rejects_foreign_hosts_and_query_urls(self):
        for url in ("https://example.com/", URL + "?token=private", "http://" + HOST + "/"):
            xml = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + url + '</loc></url></urlset>'
            with self.assertRaises(ValueError):
                indexnow.sitemap_urls(xml, HOST)

    def test_sitemap_deduplicates_and_rejects_empty_or_index(self):
        xml = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ('<url><loc>' + URL + '</loc></url>') * 2 + '</urlset>'
        self.assertEqual(indexnow.sitemap_urls(xml, HOST), [URL])
        for xml in ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>', '<sitemapindex/>'):
            with self.assertRaises(ValueError):
                indexnow.sitemap_urls(xml, HOST)

    def test_changed_urls_include_additions_edits_and_removals_only(self):
        old = {URL: "same", URL + "edited/": "old", URL + "removed/": "old"}
        new = {URL: "same", URL + "edited/": "new", URL + "added/": "new"}
        self.assertEqual(indexnow.changed_urls(old, new),
                         [URL + "added/", URL + "edited/", URL + "removed/"])

    def test_noindex_page_is_not_added(self):
        body = ('<link rel="canonical" href="' + URL + '"><meta name="robots" content="noindex,follow">').encode()
        with patch.object(indexnow, "request", return_value=(200, body, {"Content-Type": "text/html"}, URL)):
            self.assertEqual(indexnow.page_fingerprint(URL, HOST), (URL, None))

    def test_redirect_or_wrong_canonical_aborts(self):
        for final_url, canonical in ((URL + "other/", URL), (URL, URL + "other/")):
            body = ('<link rel="canonical" href="' + canonical + '">').encode()
            with patch.object(indexnow, "request", return_value=(200, body, {"Content-Type": "text/html"}, final_url)):
                with self.assertRaises(ValueError):
                    indexnow.page_fingerprint(URL, HOST)

    def test_indexnow_status_is_not_silently_accepted(self):
        for status in (200, 202, 204):
            with patch.object(indexnow, "request", return_value=(status, b"", {}, indexnow.ENDPOINT)):
                if status == 204:
                    with self.assertRaises(RuntimeError):
                        indexnow.submit(HOST, "a" * 32, [URL])
                else:
                    self.assertEqual(indexnow.submit(HOST, "a" * 32, [URL]), status)

    def test_failed_or_pending_submission_preserves_previous_state(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / ".github").mkdir()
            key = "a" * 32
            (root / ".github/indexnow.json").write_text(json.dumps({"host": HOST, "key": key}))
            (root / (key + ".txt")).write_text(key)
            state = root / "state.json"
            original = json.dumps({URL: "b" * 64})
            state.write_text(original)
            xml = ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + URL + '</loc></url></urlset>').encode()
            def response(url):
                return 200, (xml if url.endswith("sitemap.xml") else key.encode()), {}, url
            cwd = os.getcwd()
            try:
                os.chdir(root)
                for outcome in (RuntimeError("submission failed"), 202, 200):
                    with patch("sys.argv", ["indexnow.py", "--state", str(state)]), \
                            patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                            patch.object(indexnow, "request", side_effect=response), \
                            patch.object(indexnow, "page_fingerprint", return_value=(URL, "c" * 64)), \
                            patch.object(indexnow, "submit", side_effect=outcome if isinstance(outcome, Exception) else None,
                                         return_value=outcome):
                        if isinstance(outcome, Exception):
                            with self.assertRaises(RuntimeError):
                                indexnow.main()
                        else:
                            indexnow.main()
                        self.assertEqual(json.loads(state.read_text()), {URL: ("c" if outcome == 200 else "b") * 64})
            finally:
                os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
