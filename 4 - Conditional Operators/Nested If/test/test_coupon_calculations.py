#!/usr/bin/python3
"""
Tanner Babcock
September 17, 2019

Module 4, Topic 3: Multiple and Nested if Statements
"""
import unittest
from coupon_calculations import calculate_order

class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertEqual(round(calculate_order(7.00, 5, 10), 2), 7.86)
        self.assertEqual(round(calculate_order(7.50, 5, 15), 2), 8.2)
        self.assertEqual(round(calculate_order(7.75, 5, 20), 2), 8.28)
        self.assertEqual(round(calculate_order(8.00, 10, 10), 2), 4.04)
        self.assertEqual(round(calculate_order(8.25, 11, 15), 2), 3.47)
        self.assertEqual(round(calculate_order(9.00, 12, 10), 2), 3.09)

    #def test_price_under_between_ten_thirty(self):


    #def test_price_under_between_thirty_fifty(self):

    #def test_price_under_over_fifty(self):



if __name__ == "__main__":
    unittest.main()

