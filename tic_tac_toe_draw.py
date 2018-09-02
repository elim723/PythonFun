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
    return

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
    pattens = hwinner + vwinner + dwinner
    return 1 in pattens, 2 in pattens

# function to print who wins
def print_result (p1, p2):

    line = '{0} {1} win.'
    for index, p in enumerate ([p1, p2]):
        state = 'does' if p else 'does not'
        player = player1 if index==0 else player2
        print (line.format (player, state))

# function to update board
def update_board (board, player):

    # ask for input
    text = 'which (row, col) does ' + \
           str (player) + ' want to place your move? '
    row, col = raw_input (text).split (',')
    # check if loc is already taken
    while board[int (row)][int (col)] in [1, 2]:
        text = 'your (row, col) is taken :( ' + \
               'please pick another one. '
        row, col = raw_input (text).split (',')
    # update board
    try:
        board[int (row)][int (col)] = 1 if player==player1 else 2
    except:
        valid = False
        while not valid:
            text = 'your (row, col) is invalid. ' + \
                   'please pick another one. '
            row, col = raw_input (text).split (',')
        board[int (row)][int (col)] = 1 if player==player1 else 2
    return board
        
if __name__ == "__main__":

    # set up board
    nd, filled = 3, False
    nbox, shape = nd*nd, (nd, nd)
    board = np.zeros (nbox).astype (int).reshape (shape)
    
    # start with player 1
    player1 = raw_input ('what is player 1s name? ')
    player2 = raw_input ('what is player 2s name? ')
    player = player2 # player will be switched to 1
    draw (nd, board)
    
    # loop between player 1 and 2
    # til board is filled
    while not filled:
        # step 1: switch player
        player = player1 if player==player2 else player2
        # step 2: update board
        board = update_board (board, player)
        # step 3: draw current board
        draw (nd, board)
        # step 4: check winner
        p1, p2 = who_wins (nd, board)
        # step 5: check if board filled
        filled = 0 not in board or p1 or p2

    # board is filled, who wins ?
    print_result (p1, p2)
