#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 4: Functions with variable parameter lists
"""
import unittest
from validate_input_in_functions import score_input

class ValidateInput(unittest.TestCase):
    def test_score_input_test_name(self):
        score_input("Tanner Babcock")

    def test_score_input_test_score_valid(self):
        score_input("Tanner Babcock", 90)

    def test_score_input_test_score_below_range(self):
        score_input("John Smith", -5)

    def test_score_input_test_score_above_range(self):
        score_input("Benjamin Franklin", 106)

    def test_test_score_non_numeric(self):
        try:
            score_input("Test", "hello")
        except:
            print("Bad input")

    def test_score_input_invalid_message(self):
        score_input("Hello World", -20, "oops")

if __name__ == "__main__":
    unittest.main()

