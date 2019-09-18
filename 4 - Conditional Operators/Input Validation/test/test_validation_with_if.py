#!/usr/bin/python3
"""
Tanner Babcock
September 17, 2019

Module 4, Topic 4: Input Validation
"""
import unittest
from validation_with_if import average

class MyTestCase(unittest.TestCase):
    def test_input_validation_if(self):
        self.assertEqual(-1, average(-90, 90, 95))
        self.assertEqual(-1, average(91, -95, 97))
        self.assertEqual(-1, average(90, 80, -12))

if __name__ == "__main__":
    unittest.main()

