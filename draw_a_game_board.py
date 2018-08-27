#!/usr/bin/env python

# a function to draw a grid
def draw (nbox):

    # essential grid to define boxes
    horizon = ' ---' * nbox
    row  = horizon + '\n' + '|   ' * nbox + '|'

    # loop through nboxes
    for n in range (nbox):
        print ('{0}'.format (row))

    # print the close horizontal line
    print ('{0}'.format (horizon))

# define variables
nbox = 3

# draw
draw (nbox)
