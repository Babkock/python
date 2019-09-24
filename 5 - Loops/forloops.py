#!/usr/bin/python3
"""
Tanner Babcock
September 24, 2019

Module 5, Topic 1: For loop and range()
"""
theList = [1.25, 2.74, 8.86, 3.14, 6.96]

count = 0
for iterator in theList:
    print("{0}: {1:.2f}".format(count, iterator))
    count += 1

count = 0
for iterator in range(99, 32, -1):
    if (iterator % 2) == 1:  # use x % 2 to determine odd or even
        print(iterator)

