#!/usr/bin/env python

# get users input
string = raw_input ('Give me a sentence please: ')

# reverse order
reverse = ' '.join (string.split (' ')[::-1])

# print results
print ('reversed: {0}'.format (reverse))
