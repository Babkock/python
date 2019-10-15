#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019
Module 8, topic 1: Sets in Python
"""
import unittest
from set_membership import in_set

class SetTest(unittest.TestCase):
    def test_in_set_true(self):
        a = {2, 4, 6, 8, 10}
        self.assertEqual(in_set(a, 10), True)

    def test_in_set_false(self):
        b = {1, 3, 5, 7, 9}
        self.assertEqual(in_set(b, 8), False)

if __name__ == "__main__":
    unittest.main()

