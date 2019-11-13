#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 2: Custom Exceptions
"""
import unittest
from customer_exceptions import *

class CustomExceptionsTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1002, "Boy", "George", "555-444-3333")

    def tearDown(self):
        del self.customer

    def test_customer_str(self):
        print(self.customer)

    def test_customer_bad_customer_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            bad = Customer(1, "Hello", "World", "555-444-3333")

    def test_customer_bad_first_name(self):
        with self.assertRaises(InvalidNameException):
            bad = Customer(1002, ".", "World", "555-444-3333")

    def test_customer_bad_last_name(self):
        with self.assertRaises(InvalidNameException):
            bad = Customer(1000, "Hello", ".", "444-333-5555")

    def test_customer_bad_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            badphone = "43-5"
            self.assertEqual(valid_number(badphone), False)
            bad = Customer(1003, "Hello", "World", badphone)

if __name__ == "__main__":
    unittest.main()

