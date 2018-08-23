#!/usr/bin/env python

# import
import random

# define variables
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
numbers = range (100)
a = random.sample (numbers, random.randint (1,20))
b = random.sample (numbers, random.randint (1,20))

# look for common elements in one line
larray = a if len (a) > len (b) else b
sarray = a if len (a) < len (b) else b
c = list (set ([ i for i in larray if i in sarray ]))

# print results
print ('a: {0}'.format (a))
print ('b: {0}'.format (b))
print ('common: {0}'.format (c))
