#!/usr/bin/python3
"""
Tanner Babcock
October 29, 2019
Module 10, topic 1: Encapsulation
"""
class Employee:
'''Employee Class '''
    # Constructor
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)

# Driver
emp = Employee('Ruiz', 'Matthew')  # call the constructor
emp.set_first_name('Matt')
print(emp.display())    # display() returns a str
del emp

