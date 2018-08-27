#!/usr/bin/env python

# define variables
names = {}
infile = '/data/i3home/elims/funstuff/outputs/nameslist.txt'

# get all text from file as a long string
with open (infile, 'rb') as f:
    string = f.read ()
f.close ()

# separate and group names
for name in string.split ('\n'):

    # continue if empty 
    if name == '': continue
    # counts
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1

# print results
for name, counts in names.iteritems ():
    print ('{0}: {1} counts'.format (name, counts))
