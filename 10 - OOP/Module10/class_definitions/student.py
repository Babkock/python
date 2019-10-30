#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 3: Testing Classes
"""
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if (isinstance(lname, str) != True):
            raise AttributeError("Last name is not a str type")
        if (isinstance(fname, str) != True):
            raise AttributeError("First name is not a str type")
        if (isinstance(major, str) != True):
            raise AttributeError("Major is not a str type")
        if (isinstance(gpa, float) != True):
            raise AttributeError("GPA is not a float type")
        if (gpa < 0.0) or (gpa > 4.0):
            raise AttributeError("GPA is not in the accepted range")

        self._last_name = lname
        self._first_name = fname
        self._major = major
        self._gpa = gpa

    def __str__(self):
        return self._last_name + ", " + self._first_name + " has major " + self._major + " with GPA: " + str(self._gpa)

