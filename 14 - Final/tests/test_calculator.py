#!/usr/bin/python3
"""
Tanner Babcock
GUI Calculator Final Project
"""
import unittest
import decimal
from calculator import Add
from calculator import Subtract
from calculator import Multiply
from calculator import Divide
from calculator import Calculator
from calculator import CalculatorDivideError
from calculator import CalculatorInputError

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_addition(self):
        self.calc.history = list()
        self.calc.buffer_front_back(5, 1, 0)
        self.calc.add_operation(Add(12))
        self.calc.equals()
        self.calc.places_front = 2
        self.calc.places_back = 0

        self.assertEqual(self.calc.current_buffer, 17)

    def test_division(self):
        self.calc.history = list()
        self.calc.buffer_front_back(40, 1, 0)
        self.calc.add_operation(Divide(2400))
        self.calc.equals()
        self.calc.places_front = 1
        self.calc.places_back = 0

        self.assertEqual(self.calc.current_buffer, 60)

    def test_multiplication(self):
        self.calc.history = list()
        self.calc.buffer_front_back(30, 1, 0)
        self.calc.add_operation(Multiply(40))
        self.calc.equals()
        self.calc.places_front = 3
        self.calc.places_back = 0

        self.assertEqual(self.calc.current_buffer, 1200)

    def test_bad_input(self):
        with self.assertRaises(CalculatorInputError):
            newcalc = Calculator()
            newcalc.buffer_front_back("hey", 5, 2)

    def test_buffer_front_back(self):
        with self.assertRaises(CalculatorInputError):
            newcalc = Calculator()
            newcalc.buffer_front_back(5.5, 2.2, 6)

    def test_bad_constructor(self):
        with self.assertRaises(CalculatorInputError):
            newcalc = Calculator("bad", 5, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(CalculatorDivideError):
            newcalc = Calculator(0, 1, 0)
            newcalc.add_operation(Divide(6))
            newcalc.equals()

if __name__ == "__main__":
    unittest.main()

