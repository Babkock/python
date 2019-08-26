#!/usr/bin/python3
inF = open("input.txt", "r")
lines = inF.read().splitlines()
x = 0

for line in lines:
    x += 1
    print("{}: {}".format(x, line))

inF.close()

print("File read successfully!")
exit(0)

