#!/usr/bin/python3
"""
Tanner Babcock
October 8, 2019

Module 7, topic 1: Lists
"""
import unittest
from unittest.mock import patch
from basic_list_exception import make_list

class TestList(unittest.TestCase):
    #@patch('basic_list_exception.get_input', return_value=5)
    #def test_make_list(self, input):
    #    self.assertEqual(make_list(), [5, 5, 5])

    @patch('basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            make_list()

if __name__ == "__main__":
    unittest.main()

