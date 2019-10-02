#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 5: Inner Functions and Decorators
"""

"""
This function takes a variable-length list of measurements
and returns a string giving the perimeter and the area

:param measure_list: A list of measurements, can be at least 1 and up to 2 numbers
:returns: A string with the calculated area and perimeter
:raises ValueError: If measure_list has a length of 0, or if measurements are neither ints nor floats
"""
def measurements(measure_list):
    def area(a_list):
        if len(a_list) == 0:
            raise ValueError
        elif len(a_list) == 1:
            if (isinstance(a_list[0], int) != True) and (isinstance(a_list[0], float) != True):
                raise ValueError

            return float(a_list[0] * a_list[0])
        else:
            if (isinstance(a_list[0], int) != True) and (isinstance(a_list[0], float) != True):
                raise ValueError
            if (isinstance(a_list[1], int) != True) and (isinstance(a_list[1], float) != True):
                raise ValueError

            return float(a_list[0] * a_list[1])

    def perimeter(a_list):
        if len(a_list) == 0:
            raise ValueError
        elif len(a_list) == 1:
            if (isinstance(a_list[0], int) != True) and (isinstance(a_list[0], float) != True):
                raise ValueError

            return float(a_list[0] + a_list[0] + a_list[0] + a_list[0])
        else:
            if (isinstance(a_list[0], int) != True) and (isinstance(a_list[0], float) != True):
                raise ValueError
            if (isinstance(a_list[1], int) != True) and (isinstance(a_list[1], float) != True):
                raise ValueError

            return float(a_list[0] + a_list[0] + a_list[1] + a_list[1])

    return "Perimeter = {0:.2f}, Area = {1:.02f}".format(perimeter(measure_list), area(measure_list))

