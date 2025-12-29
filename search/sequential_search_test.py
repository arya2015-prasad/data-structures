import unittest
from sequential_search import search

class TestSequentialSearch(unittest.TestCase):
    
    def test_emptyArray(self):
        self.assertEqual(search([], 5), -1)

    def test_elementExistsInSingleLengthArray(self):
        self.assertEqual(search([5], 5), 0)

    def test_elementNotExistsInSingleLengthArray(self):
        self.assertEqual(search([5], 6), -1)

    def test_elementExistsInBeginning(self):
        self.assertEqual(search([5, 6, 2, 8, 9], 5), 0)

    def test_elementExistsInEnd(self):
        self.assertEqual(search([5, 6, 2, 8, 9], 9), 4)

    def test_elementExistsInMiddle(self):
        self.assertEqual(search([5, 6, 2, 8, 9], 8), 3)

    def test_elementNotExists(self):
        self.assertEqual(search([5, 6, 2, 8, 9], 1), -1)

    def test_elementExistsInMiddleChar(self):
        self.assertEqual(search(['D', 'H', 'R', 'U', 'V'], 'U'), 3)

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