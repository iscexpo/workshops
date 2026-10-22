import unittest
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate


class RepositoryValidationTests(unittest.TestCase):
    def test_required_files_exist(self):
        self.assertEqual(validate.check_required_files(), [])

    def test_local_markdown_targets_exist(self):
        self.assertEqual(validate.check_markdown_links(), [])

    def test_reports_missing_markdown_heading_fragment(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "guide.md").write_text("# Existing heading\n", encoding="utf-8")
            (root / "index.md").write_text(
                "[valid](guide.md#existing-heading) [broken](guide.md#missing-heading)\n",
                encoding="utf-8",
            )

            with patch.object(validate, "ROOT", root):
                errors = validate.check_markdown_links()

        self.assertEqual(len(errors), 1)
        self.assertIn("Broken Markdown fragment: index.md -> guide.md#missing-heading", errors[0])

    def test_accepts_duplicate_heading_slugs_and_rejects_missing_local_fragment(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "index.md").write_text(
                "# Guide\n# Guide\n[First](#guide) [Second](#guide-1) [Missing](#nope)\n",
                encoding="utf-8",
            )

            with patch.object(validate, "ROOT", root):
                errors = validate.check_markdown_links()

        self.assertEqual(len(errors), 1)
        self.assertIn("Broken Markdown fragment: index.md -> #nope", errors[0])

    def test_checks_url_encoded_paths_and_rejects_links_outside_root(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "space name.md").write_text("# Encoded heading\n", encoding="utf-8")
            (root / "index.md").write_text(
                "[Encoded](space%20name.md#encoded-heading) [Escape](../outside.md)\n",
                encoding="utf-8",
            )

            with patch.object(validate, "ROOT", root):
                errors = validate.check_markdown_links()

        self.assertEqual(len(errors), 1)
        self.assertIn("Link escapes repository: index.md -> ../outside.md", errors[0])


if __name__ == "__main__":
    unittest.main()
