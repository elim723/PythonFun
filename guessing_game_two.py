#!/usr/bin/env python

# import
import random, time

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
time.sleep (5)

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
    index = ranges.index (mynum)
    head = 0 if is_smaller else index
    tail = index if is_smaller else None

    # new range list
    head = max (minN, head)
    tail = None if tail==None else min (maxN, tail)
    ranges = ranges[head:tail]

print ('I got it in {0} trials. Not too bad hah!'.format (int (ntrials)))
print ('Bye :)')
    
    
