#!/usr/bin/python3
"""
Tanner Babcock
November 19, 2019
Module 13, topic 1: GUI and Data Visualization
"""
import unittest
from number_guess import NumberGuesser

class TestNumberGuess(unittest.TestCase):
    def setUp(self):
        self.guesser = NumberGuesser()

    def tearDown(self):
        del self.guesser

    def test_random_number(self):
        the_number = 0
        for x in range(1,7):
            self.guesser.add_guess(x)
            if self.guesser.is_winner():
                the_number = x
                break
        self.assertEqual(self.guesser.guessed_list[-1], x)

if __name__ == "__main__":
    unittest.main()

