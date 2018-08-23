#!/usr/bin/env python

# ask for user input
n = raw_input ('Give me a number please? ')
n = float (n)

# define variables
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# get list less than 5
b = [i for i in a if i < 5]
# get list less than n
c = [i for i in a if i < n]

# print
print ('a: {0}'.format (a))
print ('b: {0}'.format (b))
print ('c: {0}'.format (c))
