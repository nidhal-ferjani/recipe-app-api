"""
Sample tests
"""

from django.test import SimpleTestCase
import unittest
from app import calc


@unittest.skip('Just test how to work the SimpleTestCase')
class CalcTests(SimpleTestCase):
    """
    Class test add numbers
    """
    def test_calc_numbers(self):
        """

        :return: Test adding numbers
        """
        res = calc.add(12, 23, 10)

        self.assertEqual(res, 45)
