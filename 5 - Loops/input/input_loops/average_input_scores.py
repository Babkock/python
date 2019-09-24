#!/usr/bin/python3
"""
Tanner Babcock
September 24, 2019

Module 5, topic 2: The while loop
"""
def average(score_list):
    sum = 0
    items = len(score_list)
    
    for iterator in score_list:
        sum += iterator
    
    avg = sum / items
    return avg

if __name__ == '__main__':
    first_name = input("First name: ")
    last_name = input("Last name: ")

    try:
        scores = [];
        string = 0;
        while True:
            string = input("Please enter a score, or 'q' to quit: ")
            if string != 'q':
                scores.append(int(string))
            else:
                raise ValueError
    except:
        avg_scores = average(scores)
    finally:
        print("{0}, {1} grade: {2:.2f}".format(last_name, first_name, avg_scores))

