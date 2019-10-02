#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 4: Functions with variable parameter lists
"""
import unittest
import unittest.mock as mock
from validate_input_in_functions import score_input

class ValidateInput(unittest.TestCase):
    def test_score_input_test_name(self):
        score_input("Tanner Babcock")

    def test_score_input_test_score_valid(self):
        score_input("Tanner Babcock", 90)

if __name__ == "__main__":
    unittest.main()

