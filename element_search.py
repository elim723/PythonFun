#!/usr/bin/env python

# import
import random

# function to check if num in ordered list
#def function (olist, num):
#
#    return num in olist

# function to check by binary search
def function (olist, num):

    # keep looping until only one element left
    while not len (olist) == 1:
        # if there is no more elements,
        # num is not in list i.e. False
        if len (olist) == 0: return False
        # look for the middle index
        mdex = int (len (olist)/2.)
        # get first and last indices of new list
        head = 0 if num < olist [mdex] else mdex
        tail = mdex if num < olist [mdex] else None
        # define new list
        olist = olist [head:tail]

    # return if num is list
    return num in olist

# define variables
maxN = 100
sample = sorted (random.sample (range (1, maxN),
                                random.randint (1, maxN)))
anum = random.randint (1, maxN)

# print result
print ('a number: {0}'.format (anum))
print ('list ({0}): {1}'.format (len (sample), sample))
print ('number in list? {0}'.format (function (sample, anum)))
