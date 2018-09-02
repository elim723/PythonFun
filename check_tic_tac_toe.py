#!/usr/bin/env python

# import
import numpy as np

# a function to draw a given board
def draw (nd, board):

    horizon = ' ---' * nd
    row  = horizon + '\n' + \
           '| {0} | {1} | {2} |'
    for n in range (nd):
        print (row.format (board[n][0],
                           board[n][1],
                           board[n][2]))
    print (horizon)

# function to generate a random board
def generate_board (nd):

    # set up board
    nbox, shape = nd*nd, (nd, nd)
    board = np.zeros (nbox).astype (int)

    # player 1 starts first
    player = 1
    while 0 in board:
        # identify empty boxes
        empty = np.where (board==0)[0]
        # randomly pick from empty boxes
        rindex = np.random.choice (empty)
        # place the player there
        board [rindex] = player
        # switch player
        player = 1 if player==2 else 2
    return board.reshape (shape)

# function to any sequence
def this_wins (arrays):

    return [ np.unique (array)[0] for array in arrays
             if len (np.unique (array))==1 ]

# function to determine who win
def who_wins (nd, board):

    # check horizontal
    hwinner = this_wins (board)
    # check vertical
    vwinner = this_wins (board.T)
    # chech diagonal
    diagonal  = [ board[i][i] for i in range (0, nd) ]
    idiagonal = [ board[i][nd-1-i] for i in range (0, nd) ]
    dwinner = this_wins ([diagonal, idiagonal])
    
    # determine who wins
    p1 = 1 in hwinner + vwinner + dwinner
    p2 = 2 in hwinner + vwinner + dwinner
    return p1, p2


# function to print who wins
def print_result (p1, p2):

    line = '{0} {1} win.'
    for p in ['p1', 'p2']:
        state = 'does' if eval (p) else 'does not'
        print (line.format (p, state))
        
if __name__ == "__main__":

    # define constants
    nd = 3 
    
    # generate a board
    board = generate_board (nd)
    
    # draw the board
    draw (nd, board)
    
    # any one win?
    p1, p2 = who_wins (nd, board)

    # print result
    print_result (p1, p2)


