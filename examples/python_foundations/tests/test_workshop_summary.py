import unittest

from examples.python_foundations.workshop_summary import build_summary


class BuildSummaryTests(unittest.TestCase):
    def test_positive_activity_count(self):
        self.assertEqual(
            build_summary("Python Foundations", 3),
            "Workshop: Python Foundations\n"
            "Activities planned: 3\n"
            "Let's begin with the first activity!",
        )

    def test_zero_activity_count(self):
        self.assertEqual(
            build_summary("Web basics", 0),
            "Workshop: Web basics\n"
            "Activities planned: 0\n"
            "The activities still need to be prepared.",
        )

    def test_topic_whitespace_is_trimmed(self):
        self.assertIn("Workshop: Python", build_summary("  Python  ", 1))

    def test_empty_topic_is_rejected(self):
        with self.assertRaises(ValueError):
            build_summary("   ", 1)

    def test_negative_activity_count_is_rejected(self):
        with self.assertRaises(ValueError):
            build_summary("Python", -1)


if __name__ == "__main__":
    unittest.main()
