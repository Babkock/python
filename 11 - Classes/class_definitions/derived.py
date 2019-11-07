#!/usr/bin/python3
"""
Tanner Babcock
November 6, 2019
Module 11, topic 2: Inheritance
"""

class Person:
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

class Student(Person):


if __name__ == "__main__":

