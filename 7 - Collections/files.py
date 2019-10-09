#!/usr/bin/python3
"""
Tanner Babcock
October 8, 2019

Module 7, topic 3: Files I/O
"""

def average_scores(*args, **kwargs):
    averages = []
    first_name = ""
    for score in args:
        averages.append(score)
    total = 0
    for av in averages:
        total += av
    average = total / len(args)
    for key, value in kwargs.items():
        if (key == "course"):
            course = value
        if (key == "first_name"):
            first_name = value
        if (key == "last_name"):
            last_name = value
        print("%s == %s" % (key, value))

    return "Name = {0} {1}, GPA = {2:.2f}, Course = {3}".format(first_name, last_name, average, course)

if __name__ == "__main__":
    print(average_scores(4, 3, 2, 4, first_name = "Tanner", last_name = "Babcock", course = "Python"))
    print(average_scores(5, 6, 4, 5, 7, first_name = "Example", last_name = "Test Test", course = "Java", teacher = "Phife Dawg"))
    print(average_scores(4, 2, 4, first_name = "Ryan", last_name = "Gosling", course = "Acting", teacher = "Harrison Ford"))

