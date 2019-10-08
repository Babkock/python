#!/usr/bin/python3
import unittest
from unittest.mock import patch
from basic_list import make_list

class TestList(unittest.TestCase):
    @patch('basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        pass

