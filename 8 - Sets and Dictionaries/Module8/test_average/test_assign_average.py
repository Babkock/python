#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019
Module 8, topic 3: Selection using dictionary
"""
import unittest
from assign_average import switch_average

class SelectionTest(unittest.TestCase):
    def test_dict_a(self):
        a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
        b = switch_average(a, 'A')
        self.assertEqual(b, 90)
    
    def test_dict_b(self):
        a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
        b = switch_average(a, 'B')
        self.assertEqual(b, 80)

    def test_dict_c(self):
        a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
        b = switch_average(a, 'C')
        self.assertEqual(b, 70)

    def test_dict_d(self):
        a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
        b = switch_average(a, 'D')
        self.assertEqual(b, 60)

    def test_dict_f(self):
        a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 50 }
        b = switch_average(a, 'F')
        self.assertEqual(b, 50)

    def test_no_key(self):
        with self.assertRaises(KeyError):
            a = { 'A': 90, 'B': 80, 'C': 70, 'D': 60 }
            b = switch_average(a, 'G')

if __name__ == "__main__":
    unittest.main()

