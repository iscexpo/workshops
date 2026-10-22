import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import make_greeting


class GreetingTests(unittest.TestCase):
    def test_includes_name(self):
        self.assertEqual(
            make_greeting("A learner"),
            "Hello, A learner! Welcome to ISC Expo Workshops.",
        )

    def test_trims_outer_whitespace(self):
        self.assertEqual(
            make_greeting("  Sam  "),
            "Hello, Sam! Welcome to ISC Expo Workshops.",
        )

    def test_uses_fallback_for_blank_name(self):
        self.assertEqual(
            make_greeting("  "),
            "Hello, learner! Welcome to ISC Expo Workshops.",
        )


if __name__ == "__main__":
    unittest.main()
