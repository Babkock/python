#!/usr/bin/python3
"""
Tanner Babcock
September 24, 2019

Module 5, topic 2: The while loop
"""
import unittest
from average_input_scores import average

class LoopTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(10, average([12, 8, 10, 9, 11, 10]))

if __name__ == '__main__':
    unittest.main()

