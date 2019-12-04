#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import unittest
import decimal
from driver import add_multiple_to_buffer
from driver import add_number_after_period
from calculator import Add
from calculator import Subtract
from calculator import Multiply
from calculator import Divide
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_addition(self):
        self.calc.current_buffer = 5
        self.calc.places_front = 1
        self.calc.add_operation(Add(12))
        self.calc.equals()
        self.calc.places_front = 2
        self.calc.places_back = 0

        self.assertEqual(self.calc.current_buffer, 17)

    def test_multiplication(self):
        self.calc.history = list()
        self.calc.current_buffer = 30
        self.calc.places_front = 1
        self.calc.places_back = 0
        self.calc.add_operation(Multiply(40))
        self.calc.equals()
        self.calc.places_front = 3
        self.calc.places_back = 0

        self.assertEqual(self.calc.current_buffer, 1200)

if __name__ == "__main__":
    unittest.main()

