import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate


class RepositoryValidationTests(unittest.TestCase):
    def test_required_files_exist(self):
        self.assertEqual(validate.check_required_files(), [])

    def test_local_markdown_targets_exist(self):
        self.assertEqual(validate.check_markdown_links(), [])


if __name__ == "__main__":
    unittest.main()
