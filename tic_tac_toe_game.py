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

# check if valid
def isvalid (board, row, col):
    
    # check if loc is already taken
    isempty = board[row][col] == 0
    nd = len (board)
    isvalid = isempty or (row in range (0, nd) and col in range (0, nd))
    return isvalid
    
# function to update board
def update_board (board, player):

    valid = False
    while not valid:
        # ask for input
        text = 'which (row, col) does ' + \
               str (player) + ' want to place your move? '
        row, col = raw_input (text).split (',')
        row, col = int (row), int (col)
        valid = isvalid (board, row, col)

    board[row][col] = 1 if player==player1 else 2
    return board
        
if __name__ == "__main__":

    # set up board
    nd = 3
    nbox, shape = nd*nd, (nd, nd)
    
    # get players' names
    player1 = raw_input ('what is player 1s name? ')
    player2 = raw_input ('what is player 2s name? ')

    # start game
    np1, np2 = 0, 0
    cont = True

    while cont:

        # start with player 1
        # player will be switched to 1
        player = player2

        # set up empty box
        filled = False
        board = np.zeros (nbox).astype (int).reshape (shape)
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
        if p1: np1 += 1
        if p2: np2 += 1

        # ask if cont
        iscont = raw_input ('keep going (true/false)? ')
        cont = iscont.lower () == 'true'

        # if not cont
        if not cont:
            print ('{0} won {1} times.'.format (player1, np1))
            print ('{0} won {1} times.'.format (player2, np2))
