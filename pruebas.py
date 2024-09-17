# test_roman_converter.py
import unittest
from codido import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_convert_I(self):
        self.assertEqual(roman_to_int("I"), 1)

    def test_convert_V(self):
        self.assertEqual(roman_to_int("V"), 5)

    def test_convert_X(self):
        self.assertEqual(roman_to_int("X"), 10)

    def test_convert_II(self):
        self.assertEqual(roman_to_int("II"), 2)

if __name__ == '__main__':
    unittest.main()