#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 3: Testing Classes
"""
import unittest
from student import Student

class ClassTest(unittest.TestCase):
    def setUp(self):
        self.student = Student("Appleseed", "Johnny", "Apples", 4.0)

    def tearDown(self):
        del self.student

if __name__ == "__main__":
    unittest.main()

