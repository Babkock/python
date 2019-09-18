#!/usr/bin/python3
"""
Tanner Babcock
September 17, 2019

Module 4, topic 2: Basic input and output
"""
def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score1 < 0:
        raise ValueError
    if score2 < 0:
        raise ValueError
    if score3 < 0:
        raise ValueError

    # convert all input strings to floats, then compute
    return float((score1 + score2 + score3) / NUMBER_TESTS)

if __name__ == '__main__':
    # get first name, last name, and age
    try:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        age = input("Age: ")
        # get average
        score1 = input("First score: ")
        score2 = input("Second score: ")
        score3 = input("Third score: ")
        average_scores = average(int(score1), int(score2), int(score3))

        # print average_scores with only 2 decimal places
        print("{0}, {1} age: {2} average grade: {3:.2f}".format(first_name, last_name, age, average_scores))
    except:
        print("An exception occurred.")

