#!/usr/bin/python3
"""
Tanner Babcock
September 24, 2019

Module 4, topic 2: The while loop
"""

if __name__ == '__main__':
    theList = []
    go = input("Enter a number, or 'q' to quit: ")
    while go != 'q':
        # check if the user typed 'q' or not
        while go.isdigit() == False:
            # get input again if it's not really a number
            go = input("Please enter a number: ")
        theList.append(go)
        # append to theList
        go = input("Enter a number, or 'q' to quit: ")

    count = 0
    for iterator in theList:
        print("{0}: {1}".format(count, iterator))
        count += 1

