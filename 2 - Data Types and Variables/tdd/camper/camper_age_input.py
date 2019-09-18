#!/usr/bin/python3
"""
Tanner Babcock
September 10, 2019

Module 2, Topic 5: Test-driven development
"""

def convert_to_months(years):
    months = (years * 12)
    return months

if __name__ == '__main__':
    age_in_years = input("Age in years: ")
    age_in_months = convert_to_months(int(age_in_years))

    print("{} years is {} months".format(age_in_years, age_in_months))

# Example input: 3
# Expected output: 3 years is 36 months

