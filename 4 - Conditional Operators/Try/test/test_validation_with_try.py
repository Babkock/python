#!/usr/bin/python3
"""
Tanner Babcock
September 17, 2019

Module 4, Topic 4: Input Validation
"""
import unittest
from validation_with_try import average

class MyTestCase(unittest.TestCase):
    def test_input_validation_if(self):
        with self.assertRaises(ValueError):
            average(-90, 40, 80)

        with self.assertRaises(ValueError):
            average(80, -95, 92)

        with self.assertRaises(ValueError):
            average(90, 80, -30)


if __name__ == "__main__":
    unittest.main()

