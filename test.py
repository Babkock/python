#!/usr/bin/python3
outF = open("output.txt", "w")
contents = ["One", "Two", "Three", "Four", "Five"]

for line in contents:
    outF.write(line)
    outF.write("\n")
outF.close()

print("File written successfully!\n")
exit(0)

