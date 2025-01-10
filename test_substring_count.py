import unittest
from SubstringCount import substring_count

class TestSubstringCount(unittest.TestCase):
    """Unit tests for the substring_count function."""

    def test_basic_case(self):
        self.assertEqual(substring_count('APT APT APT', 'APT'), 3)

    def test_no_occurrences(self):
        self.assertEqual(substring_count('Python is fun', 'APT'), 0)

    def test_partial_match(self):
        self.assertEqual(substring_count('APT APTAPT APT', 'APT'), 4)

    def test_empty_main_string(self):
        self.assertEqual(substring_count('', 'APT'), 0)

    def test_empty_substring(self):
        self.assertEqual(substring_count('APT APT APT', ''), 0)

    def test_both_empty(self):
        self.assertEqual(substring_count('', ''), 0)

if __name__ == '__main__':
    unittest.main()