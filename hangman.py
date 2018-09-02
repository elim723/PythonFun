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

# function to deal with user guesses
def get_user (guesses):

    # get user input
    user = raw_input ('| make a guess: ').lower ()
    # check user input
    invalid = user in guesses
    while invalid:
        user = raw_input ('| try again: ')
        invalid = user in guesses
    guesses.append (user)
    return user, guesses

# function to update current
def update_current (length, current, user, word):
    
    indices = [ i for i in range (length) if word[i]==user ]
    for index in indices:
        current[index] = user
    return current

# function to define end result
def end_result (word, current, correct, nwrong, ntrials):

    # win if correct
    if correct:
        print ('| you got it in {0} trials :)'.format (ntrials))
    else:
        print ('| sorry .. you ran out of wrong guesses ({0}) :('.format (nwrong))
    print ('| The word is {0}.'.format (word))
    return correct

# function to start a game
def a_game (word):

    length = len (word)
    current = ['_'] * length
    pcurrent = ''.join (current)    
    # print
    print ('| Welcome to Hangman !')
    print ('| current: {0}'.format (pcurrent))
    # set up
    cont, guesses = True, []
    ntrials, nwrong = 0, 0

    while cont:

        # deal with user guesses
        user, guesses = get_user (guesses)
        # replace _ by guesses
        current = update_current (length, current, user, word)
        # print current
        pcurrent = ''.join (current)
        print ('| current: {0}'.format (pcurrent))
        # increment trials
        ntrials += 1
        if user not in word:
            nwrong += 1
            draw_hangman (nwrong)
            #print ('| max 6 wrong guesses; you have {0} left ...'.format (6 - nwrong))

        # check if keep going
        correct = pcurrent == word
        cont = not (correct or nwrong >= 6)
    return current, correct, nwrong, ntrials

# function to draw hangman
def draw_hangman (nwrong):

    # top
    print ('+{0}'.format ('-'*7))
    print ('|   |   ')
    # head
    line = '|  / \  ' if nwrong >= 1 else '|'
    print (line)
    line = '|  \ /  ' if nwrong >= 1 else '|'
    print (line)
    # body 1
    line = '|   |   ' if nwrong >= 2 else '|'
    print (line)
    # body 2 + arms
    line = '|   |   ' if nwrong == 2 else \
           '|  /|   ' if nwrong == 3 else \
           '|  /|\  ' if nwrong >= 4 else '|'
    print (line)
    # body 3
    line = '|   |   ' if nwrong >= 2 else '|'
    print (line)
    # body 4
    line = '|  /    ' if nwrong == 5 else \
           '|  / \  ' if nwrong == 6 else '|'
    print  (line)
    # end
    print ('|')

# function to start new round
def new_round ():

    # pick random word
    word = pick_word ()

    # run a game
    args = a_game (word)
    
    # end result
    end_result (word, *args)
    return args[1]

if __name__ == "__main__":

    # start with set up
    nwin, cont = 0, True

    # loop if keep playing
    while cont:
        print ('+-------------------------------------')
        correct = new_round ()
        # keep track of # wins
        if correct: nwin =+ 1
        keepgoing = raw_input ('| Would you like to play the next round? ')
        cont = keepgoing.lower () in ['y', 'yes']
        print ('|')

    # print end result
    print ('| You have won {0} rounds!'.format (nwin))
    print ('| bye!')
