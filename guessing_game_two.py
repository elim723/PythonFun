#!/usr/bin/env python

# import
import random

# function to  interact wtih user
def interact (mynum):

    print ('my guess is {0}'.format (mynum))
    # is it correct?
    correct = raw_input ('is my guess correct? ')
    if correct in ['yes', 'y']: return True, -1
    # not correct .. is my guess too high?
    is_smaller = raw_input ('is my guess value too large? ')
    return False, is_smaller.lower () in ['yes', 'y']

# define variables
minN, maxN = 0, 100
ranges = range (minN, maxN)

# tell user to have a number!
print ('Please have a number between {0} and {1} in your head.'.format (minN, maxN-1))

# guess
ntrials = 0.
correct = False
while not correct:

    # increment number of trials
    ntrials += 1.

    # computer guess a number
    mynum = random.randint (ranges[0], ranges[-1])
    correct, is_smaller = interact (mynum)
    if correct: break
    
    # figure out a list to check
    head = 0 if is_smaller else mynum
    tail = mynum if is_smaller else None
    print ('head, tail: {0}, {1}'.format (head, tail))

    # new range list
    head, tail = max (minN, head), min (maxN, tail)
    ranges = ranges[head:tail]
    print ('new range: {0}'.format (ranges))

print ('Bye :)')
    
    
