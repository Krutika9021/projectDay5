# test_main.py
import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Positive numbers

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  # Negative numbers

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)  # Mixed positive and negative

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)  # Both zero
        self.assertEqual(add(5, 0), 5)  # One zero
        self.assertEqual(add(0, 5), 5)  # One zero

if __name__ == "__main__":
    unittest.main()
