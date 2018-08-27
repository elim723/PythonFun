#!/usr/bin/env python

# get two files
fprime = '/data/i3home/elims/funstuff/outputs/prime_numbers.txt'
fhappy = '/data/i3home/elims/funstuff/outputs/happy_numbers.txt'

with open (fprime, 'rb') as f:
    prime = f.read ()
f.close ()
with open (fhappy, 'rb') as f:
    happy = f.read ()
f.close ()

# redefine numbers
prime = [ int (n) for n in prime.split ('\n') if len (n)>0 ]
happy = [ int (n) for n in happy.split ('\n') if len (n)>0 ]

# comapre numbers
sarray = prime if len (prime) < len (happy) else happy
larray = prime if len (prime) > len (happy) else happy

common = [ n for n in larray if n in sarray ]

# print result
print ('unique prime: {0}'.format (set (prime)))
print ('unique happy: {0}'.format (set (happy)))
print ('common elements: {0}'.format (common))
