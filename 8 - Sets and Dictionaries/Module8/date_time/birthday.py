#!/usr/bin/python3
"""
Tanner Babcock
October 15, 2019
Module 8, topic 4: datetime
"""
from datetime import datetime, timedelta

def half_birthday(birthday):
    return birthday + timedelta(days=182)

if __name__ == "__main__":
    date_string = input("Enter a date in the format \"MM DD YYYY\":")
    date_object = datetime.strptime(date_string, "%m %d %Y")
    half = half_birthday(date_object)
    print("Your half birthday: ", str(half))

