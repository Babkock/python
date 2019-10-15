#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019

Module 8, topic 2: Dictionaries
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

