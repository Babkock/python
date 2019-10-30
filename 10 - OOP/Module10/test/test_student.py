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

    def test_object_created_required_attributes(self):
        test = Student("Bunyan", "Paul", "Woodworking")

    def test_object_created_all_attributes(self):
        test = Student("Ruth", "Babe", "Baseball", 3.8)

    def test_student_str(self):
        print(str(self.student))

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(AttributeError):
            test = Student(5, "Hello", "World")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(AttributeError):
            test = Student("Hello", 5, "World")

    def test_object_not_created_error_major(self):
        with self.assertRaises(AttributeError):
            test = Student("Hello", "World", 5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(AttributeError):
            test = Student("Washington", "George", "Honesty", "test")

if __name__ == "__main__":
    unittest.main()

