#!/usr/bin/python3
import csv
from county import County

with open("ExampleCSV.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # Initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it's the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[0])] = County(row[1], row[2])
    
    print(county)

