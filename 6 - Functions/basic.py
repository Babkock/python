#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 1: Function and function calls
"""

def hourly_employee_input(name, hours, wage):
    try:
        if (isinstance(name, str) != True):
            raise ValueError
        if (isinstance(hours, int) != True):
            raise ValueError
        if (isinstance(wage, float) != True):
            raise ValueError
        print("{0} worked {1} hours at ${2:.2f}".format(name, hours, wage))
    except:
        print("Bad input")

if __name__ == '__main__':
    hourly_employee_input("Tanner Babcock", 40, 12.50)
    hourly_employee_input(10, "test", -5)

