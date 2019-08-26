#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description='Process')
parser.add_argument("-file", help='The file to read', required=True)
args = parser.parse_args()

inF = open(args.file, "r")
lines = inF.read().splitlines()
x = 0

for line in lines:
    x += 1
    print("{}: {}".format(x, line))

inF.close()

print("File read successfully!")
exit(0)

