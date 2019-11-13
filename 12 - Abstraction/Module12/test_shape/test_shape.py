#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 4: Testing Abstract Classes
"""
import unittest
from shape import InvalidSideError
from shape import Rectangle
from shape import Shape

class RectangleClassTest(unittest.TestCase):
    def setUp(self):
        self.shape = Rectangle(12, 23.4)

    def tearDown(self):
        del self.shape

    def test_constructor(self):
        with self.assertRaises(InvalidSideError):
            r = Rectangle(5, -5)
        with self.assertRaises(InvalidSideError):
            r = Rectangle(-5, 5)

    def test_shape_area(self):
        self.assertAlmostEqual(280.8, self.shape.area())

if __name__ == "__main__":
    unittest.main()

