#!/usr/bin/env python

# import
import numpy as np

# define variables
options = np.array (['paper', 'scissors', 'rock'])

# define functions
def is_cheating (user1, user2):

    for u in ['user1', 'user2']:
        if not eval (u) in options:
            raise ValueError (u + ', do not cheat!')

def again ():
    
    # print gap for end of round
    print ('')
    # ask if want to play again
    again = raw_input ('want to play again? ')
    return again.lower() in ['yes', 'y']

### while loop starts
play = True
while play:

    # get user's input
    user1 = raw_input ('user 1 turn: ')
    user2 = raw_input ('user 2 turn: ')
    is_cheating (user1, user2)
    u1 = np.where (user1==options)[0][0]
    u2 = np.where (user2==options)[0][0]

    # check for tied
    if u1==u2:
        # print results
        print ('You tied !')
        play = again ()
        continue

    # who wins?
    u1win = (u1, u2) in [(0, 2), (2, 1), (1, 0)]
    
    # print results
    msg = 'User 1' if u1win else 'User 2'
    print ('{0} win!'.format (msg))
    play = again ()
    
print ('thanks for playing! Bye :)')
