#!/usr/bin/env python

# import
import random

# define variables
numbers = range (1000, 10000)
comp = str (random.sample (numbers, 1)[0])

# check cows and bulls
def cows_and_bulls (user):

    # game over if correct guess
    if user==comp: return -1

    # count ncows / nbulls
    ncows, nbulls = 0, 0 
    for n in range (4):
        cdigit, udigit = comp [n], user [n]
        # if same digit at the same place, cow!
        if cdigit == udigit: ncows += 1
        else:
            # if the digit in comp, bull!
            if udigit in comp: nbulls += 1
    return ncows, nbulls

# while loop
correct = False
while not correct:

    # ask user
    user = raw_input ('Guess a 4 digit number: ')

    # break if exit 
    if user=='exit':
        print ('bye!'); break

    try:
        # check cow and bull
        result = cows_and_bulls (user)
    except:
        print ('please input a 4 digit guess!')
        continue

    # stop when correct guess
    if result == -1:
        correct = True; continue
    
    # print out # cows and bulls
    print ('{0} cows and {1} bulls.'.format (result[0], result[1]))
