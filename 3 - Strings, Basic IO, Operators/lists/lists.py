#!/usr/bin/python3
#
# Tanner Babcock
# Module 3 - Topic 1
# September 3, 2019

listOne = ['tanner', 'enjoys', 'python']
print(listOne)
# should print ['tanner', 'enjoys', 'python']

# append() appends an item to the end of the list
listOne.append('and')
listOne.append('rust')
print(listOne)
# should print ['tanner', 'enjoys', 'python', 'and', 'rust']

# clear() removes all items from the list
listOne.clear()
print(listOne)
# should print []

# copy() returns a copy of the list
listTwo = listOne.copy()
string = 'hello'

listTwo.append(string)
listTwo.append('world')
listTwo.append(string)
print(listTwo) # ['hello', 'world', 'hello']

# count() returns the number of occurrences of the
# given string in the list
print("'{}' occurs {} times in this list: {}".format(string, listTwo.count('hello'), listTwo))

# extend() appends multiple elements to the end of a list
listThree = ['tanner', 'doesnt', 'care', 'for']
listThree.extend(['the', 'beatles'])
print(listThree)

# index() returns the index of the given list item, starting from 0
print(listThree.index('beatles'))
# should print 5

# insert() inserts an item at the given location in the list
listThree.insert(2, 'exactly')
print(listThree)
# should print 'tanner', 'doesnt', 'exactly', 'care', 'for', 'the', 'beatles'

# remove() removes the specified element from the list
listThree.remove('for')
listThree.remove('the')
listThree.remove('beatles')
print(listThree)
# should print 'tanner', 'doesnt', 'exactly', 'care'

# reverse() reverses the list
listThree.reverse()
print(listThree)
# should print 'care', 'exactly', 'doesnt', 'tanner'

# sort() sorts the list in place
listThree.sort()
print(listThree)
# should print 'care', 'doesnt', 'exactly', 'tanner'
# this list is now alphabetized

