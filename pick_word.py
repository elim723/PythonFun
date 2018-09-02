#!/usr/bin/env python

# import
import random

# function to pick random word
def pick_word ():

    # open file
    with open ('outputs/sowpods.txt', 'rb') as f:
        words = f.read ()
    f.close ()
    words = words.split ('\n')
    # return a random word
    return random.choice (words)

if __name__ == "__main__":

    # pick random word
    word = pick_word ()

    print ('random word: {0}'.format (word))
