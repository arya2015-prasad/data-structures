import unittest
from str_search import substr

class TestStringSearch(unittest.TestCase):
    def test_emptyStringEmptySubstring(self):
        self.assertEqual(substr("", ""), -1)

    def test_emptyStringNonEmptySubstring(self):
        self.assertEqual(substr("", "hello"), -1)

    def test_nonEmptyStringEmptySubstring(self):
        self.assertEqual(substr("hello world", ""), -1)

    def test_nonEmptyStringNonExistingSubstring(self):
        self.assertEqual(substr("hello world", "worlk"), -1)

    def test_nonEmptyStringExistingSubstring(self):
        self.assertEqual(substr("hello world", "world"), 6)

    def test_nonEmptyStringExistingSubstringWithMultipleMatchingFirstCharacter(self):
        self.assertEqual(substr("hello world", "ld"), 9)

    def test_nonEmptyStringExistingSubstringWithMultipleMatches(self):
        self.assertEqual(substr("hello world! look its beautiful day", "lo"), 3)

if __name__ == "__main__":
    unittest.main()