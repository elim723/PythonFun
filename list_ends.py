#!/usr/bin/env python

# define function
def head_and_tail (array):

    return [array[0], array[-1]]

# define variables
a = [5, 10, 15, 20, 25]

# get head and tail
ht = head_and_tail (a)

# print results
print ('a: {0}'.format (a))
print ('head and tail: {0}'.format (ht))
