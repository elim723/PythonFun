#!/usr/bin/env python

# import
import random

# a function to generate lists
def get_lists (num):

    alist = [ subs [random.randint (0, len (subs)-1)] for n in xrange (num) ]
    ulist = list (set (alist))
    return alist, ulist

# generate a list
subs = ['math', 'phys', 'eng', 'chem', 'bio', 'music']

# select unique
alist, ulist = get_lists (10)

# print result
print ('orig list  : {0}'.format (alist))
print ('unique list: {0}'.format (ulist))
