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

