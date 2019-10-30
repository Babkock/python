#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 3: Testing Classes
"""
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self._last_name = lname
        self._first_name = fname
        self._major = major
        self._gpa = gpa

    def __str__(self):
        return self._last_name + ", " + self._first_name + " has major " + self._major + " with GPA: " + str(self._gpa)

