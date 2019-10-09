#!/usr/bin/python3
"""
Tanner Babcock
October 8, 2019

Module 7, topic 3: File I/O
"""
import os

def write_to_file(*args):
    output = open("student_info.txt", "a")
    
    for item in args:
        if (isinstance(item, tuple)):
            output.write("\nScores:\t\t")
            for score in item:
                output.write("{}, ".format(score))
        else:
            output.write("{}\t".format(item))
    
    output.write("\n")
    output.close()

def get_student_info(**kwargs):
    scores = ()
    for key, value in kwargs.items():
        if (key == "first_name"):
            first_name = value
        if (key == "last_name"):
            last_name = value
    s = ""

    while True:
        try:
            s = int(input("Enter a test score, or 'q' to stop: "))
            scores += (s,)
        except ValueError:
            break
    write_to_file(first_name, last_name, scores)

def read_from_file(name):
    if (isinstance(name, str) != True):
        raise ValueError
    file_dir = os.path.dirname(__file__)
    
    inp = open(os.path.join(file_dir, name), "r")
    lines = inp.read().splitlines()

    for line in lines:
        print(line)
    inp.close()
    del lines

if __name__ == "__main__":
    print("Entering test scores for student 1")
    get_student_info(first_name="Tanner", last_name="Babcock")
    print("Entering test scores for student 2")
    get_student_info(first_name="Bob", last_name="Dylan")
    print("Entering test scores for student 3")
    get_student_info(first_name="Barack", last_name="Obama")
    print("Entering test scores for student 4")
    get_student_info(first_name="Barry", last_name="Bonds")

    read_from_file("student_info.txt")

