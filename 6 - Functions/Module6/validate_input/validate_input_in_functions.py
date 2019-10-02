#!/usr/bin/python3
"""
Tanner Babcock
October 1, 2019

Module 6, topic 4: Functions with variable parameter lists
"""

"""
This function prints the test name and test score. It asks for
user input if the score is not in the valid range.

:param test_name: The name of the test taker
:param test_score: The score of the test, should be in the 0-100 range
:param invalid_message: The message to print if test_score is invalid
:raises ValueError: If test_score is not an integer type
"""
def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    if (isinstance(test_score, int) != True):
        raise ValueError
    if test_score in range(0, 100):
        print("{}: {}".format(test_name, test_score))
    else:
        print(invalid_message)
        while not 0 <= test_score <= 100:
            get_score = int(input("Please enter a valid score: "))
            test_score = get_score
        print("{}: {}".format(test_name, test_score))
    # return { test_name : test_score }

