#!/usr/bin/python3
"""
Tanner Babcock
September 10, 2019

Module 2, Topic 5: Test-driven development
"""
import unittest
from camper_age_input import convert_to_months

class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(convert_to_months(10), 120)

if __name__ == "__main__":
    unittest.main()

