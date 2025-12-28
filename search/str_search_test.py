import unittest
from str_search import search

class TestStringSearch(unittest.TestCase):
    def test_eib(self):
        self.assertEqual(search(["U", "S", "A"], "U"), 0)
    
    def test_eie(self):
        self.assertEqual(search(["U", "A", "E"], "E"), 2)
    
    def test_eim(self):
        self.assertEqual(search(["U", "K", "R", "A", "I", "N", "E"], "A"), 3)
    
    def test_MTa(self):
        self.assertEqual(search([], "D"), -1)

    def test_ede(self):
        self.assertEqual(search(["D", "H", "R", "U", "V"], "A"), -1)

if __name__ == "__main__":
    unittest.main()