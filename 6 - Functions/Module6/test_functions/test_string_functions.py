#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 3: Function parameters
"""
import unittest
from string_functions import multiply_string

class MultiplyString(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual(multiply_string("hello", 3), "hellohellohello")
        self.assertEqual(multiply_string("test", 4), "testtesttesttest")

if __name__ == "__main__":
    unittest.main()

