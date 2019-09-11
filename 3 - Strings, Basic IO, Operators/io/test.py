#!/usr/bin/python3
"""
Tanner Babcock
September 10, 2019

Module 3, Topic 2: Basic input and output
"""
import unittest
import unittest.mock as mock
import average_scores

class MyTestCase(unittest.TestCase):

    def test_average(self):

        # this supplies mock data to the input() calls in average()
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert average_scores.average() == 90


# run unit tests
if __name__ == '__main__':
    unittest.main()

