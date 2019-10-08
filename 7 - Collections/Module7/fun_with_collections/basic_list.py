#!/usr/bin/python3
"""
Tanner Babcock
October 8, 2019

Module 7, topic 1: Lists
"""

def make_list():
    x = 0
    theList = [0, 0, 0]
    for x in range(0, 3):
        theList[x] = int(input("Enter an int number: "))
    return theList

def get_input():
    pass

if __name__ == "__main__":
    try:
        myList = make_list()
        print("{}, {}, {}".format(myList[0], myList[1], myList[2]))
    except:
        print("Bad input")
