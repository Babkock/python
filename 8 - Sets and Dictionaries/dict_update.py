#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019

Module 8, topic 2: Dictionaries
"""

"""
This function calculates the average of all items in the dictionary

:param scores: The dictionary of test scores
:returns: The average of all test scores
"""
def average_scores(scores):
    if (scores != -1):
        total = 0
        for num, score in scores.items():
            total += score
        return total / len(scores)
    else:
        return -1

"""
This function gets the specified number of test scores from the user,
and fills a dictionary with them

:returns: The dictionary of scores input by the user, or -1 if the input was bad
:raises ValueError: If the input is not an integer
"""
def get_test_scores():
    try:
        num_scores = int(input("Enter the number of test scores: "))
        scores_dict = dict()
        x = 1
        while x <= num_scores:
            score = int(input("Test score number {}: ".format(x)))
            scores_dict.update({x : score})
            x += 1
        return scores_dict
    except ValueError:
        print("Bad input")
        return -1

if __name__ == "__main__":
    scores = get_test_scores()
    print(scores)
    print("Average of scores: {}".format(average_scores(scores)))

