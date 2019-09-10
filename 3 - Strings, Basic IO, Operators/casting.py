#!/usr/bin/python3
"""
Program: casting.py
Author: Tanner Babcock
Last date modified: 09/10/2019

The purpose of this program is to accept any input
and convert to an integer type.
"""
choice = input("Enter a number: ")
test = float(choice)
print("{}".format(int(test)))

exit(0)

# Input     --  Expected output      -- Actual
# 5             5                       5
# 5.6           5                       5
# 12.2          12                      12

