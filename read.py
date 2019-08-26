#!/usr/bin/python3
inF = open("input.txt", "r")
lines = inF.read().splitlines()

for line in lines:
    print("{}".format(line))

inF.close()

print("File read successfully!")
exit(0)

