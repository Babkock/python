#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 3: Function parameters
"""

def multiply_string(message, n):
    if (isinstance(message, str) != True):
        raise ValueError
    if (isinstance(n, int) != True):
        raise ValueError
    x = 0
    total = ""
    while x < n:
        total += message
        x += 1
    return total


