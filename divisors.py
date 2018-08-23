#!/usr/bin/env python

# ask for user's input
num = raw_input ('Give me a number please? ')
num = float (num)

# define a long range of test numbers
numbers = range (1, 999)

# get divisors
divisors = [n for n in numbers if num%n==0.]

# print results
print ('divisors of {0}: {1}'.format (num, divisors))
