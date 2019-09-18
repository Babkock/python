#!/usr/bin/python3
"""
Tanner Babcock
September 10, 2019

Module 3, topic 2: Basic input and output
"""
def average():
    # get 3 scores from the user
    score1 = input("Enter the first score: ")
    score2 = input("Enter the second score: ")
    score3 = input("Enter the third score: ")

    # convert all input strings to floats, then compute
    total = (float(score1) + float(score2) + float(score3)) / 3;
    return total

if __name__ == '__main__':
    # get first name, last name, and age
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = input("Age: ")
    # get average
    average_scores = average()

    # print average_scores with only 2 decimal places
    print("{0}, {1} age: {2} average grade: {3:.2f}".format(first_name, last_name, age, average_scores))
    exit(0)

