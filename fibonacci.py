#!/usr/bin/env python

# a function to generate fibonacci sequences
def fibonacci (numbers):
    a, b = 0, 1
    array = []
    for n in range (numbers):
        a, b = b, a+b
        array.append (a)
    return array


# get users input
num = int (raw_input ('Give me an integer number please: '))

# print results
print ('The Fibonacci sequeunce with {0} numbers is {1}'.format (num, fibonacci (num)))
