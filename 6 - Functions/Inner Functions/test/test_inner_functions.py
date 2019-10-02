#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 5: Inner functions and Decorators
"""
import unittest
from inner_functions_assignment import measurements

class InnerFunctionsTest(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(measurements([2.1, 3.4]), "Perimeter = 11.00, Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(measurements([3.5]), "Perimeter = 14.00, Area = 12.25")

    def test_invalid_input(self):
        try:
            measurements(["hello", "world"])
        except:
            print("Value error raised")
            pass

if __name__ == "__main__":
    unittest.main()

