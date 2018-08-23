#!/usr/bin/env python

# ask for user input
string = raw_input ('Give me a string please? ')

# is it a palindrome
is_palindrome = string==string[::-1]

# print results
msg = 'is' if is_palindrome else 'is not'
print ('your string {0} a palindrome'.format (msg))
print ('string  : {0}'.format (string))
print ('inverted: {0}'.format (string[::-1]))
