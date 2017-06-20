from twisted.trial import unittest
from fractions import Fraction

class TestSuccess(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(Fraction(19, 12),
                         Fraction(3, 4) + Fraction(5, 6))
 
    def test_add_negative(self):
        self.assertEqual(Fraction(-19, 12),
                         Fraction(-3, 4) + Fraction(-5, 6))
 
    def test_add_zero(self):
        self.assertEqual(Fraction(1, 2),
                         Fraction(0, 1) + Fraction(1, 2))
