from twisted.trial import unittest
from fractions import Fraction


class TestFractionMethodCalled(unittest.TestCase):
   def setUp(self):
       self.counter = 0

       def called(*args, **kwargs):
           self.counter += 1
           self.old_add = Fraction.__add__
       Fraction.__add__ = called

   def tearDown(self):
       Fraction.__add__ = self.old_add

   def test_add_calls_fraction_add(self):
       """
       Adding two Fractions together calls the __add__ method
       of Fraction
       """
       Fraction(1, 1) + Fraction(1, 1)
       self.assertEqual(1, self.counter)
