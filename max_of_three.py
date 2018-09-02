#!/usr/bin/env python

# function to determine the max
def nmax (args):

    nmax = args[0]
    for arg in args[1:]:
        nmax = arg if arg > nmax else nmax
    return nmax

if __name__ == '__main__':

    # get three numbers from user
    text = 'give me 3 numbers (n1, n2, n3): '
    ns = raw_input (text).split (',')
    ns = [float (n) for n in ns]

    # get nmax number
    n = nmax (ns)

    # print result
    line = 'your maximum value: {0}'
    print (line.format  (n))

    
    
