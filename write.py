#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description='Process')
parser.add_argument("-file", help='The output file to write', required=True)
args = parser.parse_args()

outF = open(args.file, "w")
contents = ["One", "Two", "Three", "Four", "Five"]

for line in contents:
    outF.write(line)
    outF.write("\n")
outF.close()

print("File written successfully!")
exit(0)

