#!/usr/bin/env python

# get raw input
num = raw_input ('Give me a number please? ')
check = raw_input ('Give me another number please? ')
num, check = float (num), float (check)

# check if it is even or odd
x2 = True if num % 2 == 0. else False
x4 = True if num % 4 == 0. else False
xcheck = True if num % check == 0. else False

# print out message
line = 'your input, {0}, is {1}.'
msg  = 'multiple of '+str (check) if xcheck else \
       'multiple of 4' if x4 else \
       'an even number' if x2 else \
       'an odd number'
print (line.format (num, msg))
