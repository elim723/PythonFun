#!/usr/bin/env python

# import 
import random

# generate a random number
ran = random.randint (1, 9)

# start while loop
ntrials = 0
correct = False
while not correct:

    # ask for users' input
    ntrials += 1
    num = raw_input ('guess a number between 1 and 9: ')

    # operations
    try:
        ## if exit
        if num == 'exit':
            print ('Bye!'); break
        ## if number
        num = float (num)
        if num == ran:
            print ('You got it in {0} trials, congrats!'.format (ntrials))
            correct = True
        elif num < ran:
            print ('guess a larger number!')
        else:
            print ('guess a smaller number!')
    except:
        print ('guess a number !')
