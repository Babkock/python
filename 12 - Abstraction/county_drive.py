#!/usr/bin/python3
"""
Tanner Babcock
November 12, 2019
Module 12, topic 1: Gathering Data using Classes
"""
import csv
from county import County

with open("Iowa 2010 Census Data Population Income.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # Initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it's the header
        if line_count == 0:
            line_count += 1
            continue
        if str(row[1]) == "United States":
            line_count += 1
            continue
        if str(row[1]) == "Iowa State":
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[1])] = County(row[2], row[3], row[4], row[5], row[6])
   
    print("Population per Household in Dallas County:\n{0:.4f}".format(county["Dallas"].population_per_household()))

    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].population.replace(',',''))
    print("Total population of Iowa:\n{}".format(pop_sum))


