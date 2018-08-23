#!/usr/bin/env python

# get user's input
num = float (raw_input ('Give me a number please: '))

# define variables
numbers = range (1, 1000)

# check divisors
divisors = list (set ([n for n in numbers if num%n==0.]))
isprime = divisors == [1, num]

# print results
msg = 'is' if isprime else 'is not'
print ('{0} {1} a prime number.'.format (num, msg))
