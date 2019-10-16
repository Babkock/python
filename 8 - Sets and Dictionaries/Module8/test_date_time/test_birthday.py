#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019
Module 8, topic 4: datetime
"""
import unittest
from datetime import datetime, timedelta
from birthday import half_birthday

class BirthdayTest(unittest.TestCase):
    def test_half_birthday(self):
        birth = "05 01 1996"
        birth_obj = datetime.strptime(birth, "%m %d %Y")
        expect = birth_obj + timedelta(days=182)

        self.assertEqual(half_birthday(birth_obj), expect)

if __name__ == "__main__":
    unittest.main()

