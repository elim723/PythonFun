#!/usr/bin/env python

# import 
import random

# define variables
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# randomly generate variables
nums = range (100)
a = random.sample (nums, 8)
b = random.sample (nums, 15)

# select common elements
larray = b if len (b) > len (a) else a
sarray = b if len (b) < len (a) else a
c = list (set ([i for i in larray if i in sarray]))

# print result
print ('a: {0}'.format (a))
print ('b: {0}'.format (b))
print ('common elements: {0}'.format (c))
