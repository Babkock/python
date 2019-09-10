#!/usr/bin/python3
#
# Tanner Babcock
# Topic 3 - Strings
# September 3, 2019

string = "Woody Allen in The Passion of Joan of Arc"

# capitalize() capitalizes the first letter in the string,
# and un-capitals all of the others
print(string.capitalize());

# find() returns the index of the given substring,
# or returns -1 if not found
test = "Passion"
print(string.find(test));
# this should print 19

# index() returns the index of the given substring,
# and throws ValueError when not found
test = "Joan"
print(string.index(test));
# this should print 30

# isalnum() returns true if all characters are alphanumeric
print(string.isalnum());
# this should return False, due to spaces

# isalpha() returns true if all characters are alphabetic
print(string.isalpha());
# this should return False, due to spaces

# isdigit() returns true if all characters are digits
print(string.isdigit());
# this should return False, as there are no digits

# islower() returns true if all characters are lowercase
print(string.islower());    # prints False

# isupper() returns true if all characters are uppercase
print(string.isupper());    # prints False

# isspace() returns true if there are only whitespace characters in the string and there is at least one character
print(string.isspace());  # False

# startswith() returns true if string starts with the given prefix
prefix = "Wood"
print(string.startswith(prefix));

exit(0);

