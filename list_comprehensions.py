#!/usr/bin/env python

# define variables
a = [1, 4, 9, 16, 25, 36, 40, 64, 81, 100]

# only even elements
even = [i for i in a if i%2==0.]

# print results
print ('even only: {0}'.format (even))
