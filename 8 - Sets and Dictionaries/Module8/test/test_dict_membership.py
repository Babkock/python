#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019
Module 8, topic 2: Dictionaries
"""
import unittest
from dict_membership import in_dict

class DictionaryTest(unittest.TestCase):
    def test_in_dict_true(self):
        a = {'A' : 90, 'B' : 80, 'C' : 70, 'D' : 20}
        self.assertEqual(in_dict(a, 'A'), True)
        self.assertEqual(in_dict(a, 'B'), True)

    def test_in_dict_false(self):
        b = {'E' : 90, 'F' : 80, 'G' : 70, 'H' : 20}
        self.assertEqual(in_dict(b, 'E'), True)
        self.assertEqual(in_dict(b, 'A'), False)
        self.assertEqual(in_dict(b, 'B'), False)

if __name__ == "__main__":
    unittest.main()

