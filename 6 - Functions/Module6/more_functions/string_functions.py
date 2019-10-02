#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 3: Function parameters
"""

"""
This function multiples the string 'message' 'n' number of times,
and returns the resulting string

:param message: The message to be multiplied
:param n: Number of times to be multiplied
:returns: 'message' multiplied 'n' times
:raises ValueError: If message or n are invalid
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


