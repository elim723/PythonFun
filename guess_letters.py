#!/usr/bin/env python

# import
import random

# function to pick random word
def pick_word ():

    # open file
    with open ('outputs/sowpods.txt', 'rb') as f:
        words = f.read ()
    f.close ()
    words = words.decode ('utf-8').split ()
    # return a random word
    return random.choice (words).lower ()

if __name__ == "__main__":

    # pick random word
    word = pick_word ()
    length = len (word)

    # print
    print ('Welcome to Hangman !')
    current = ['_'] * length
    pcurrent = ''.join (current)
    print ('pcurrent: {0}'.format (pcurrent))

    # set up
    correct = False
    guesses = []
    ntrials = 0

    # while loop
    while not correct:
        # get user input
        user = raw_input ('make a guess: ').lower ()

        # check user guesses
        invalid = user in guesses
        while invalid:
            user = raw_input ('already guessed; try again: ')
            invalid = user in guesses
        guesses.append (user)

        # replace _ by guesses
        indices = [ i for i in range (length) if word[i]==user ]
        for index in indices:
            current[index] = user

        # print current
        pcurrent = ''.join (current)
        print ('pcurrent: {0}'.format (pcurrent))

        # increment trials
        ntrials += 1
        
        # check if correct
        correct = pcurrent == word

    # print message
    print ('you got it in {0} trials :)'.format (ntrials))
