#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 2: Custom Exceptions
"""
import unittest
from customer_exceptions import Customer
from customer_exceptions import valid_number

class CustomExceptionsTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1002, "Jonathan", "George", "555-444-3333")

    def tearDown(self):
        del self.customer


