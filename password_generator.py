#!/usr/bin/env python

### import 
import string, random

### define variables
maxchar = 20.
# exclude special greek letters
characters = string.printable[:-23] 
# classify characterse for password strength
lowers = string.ascii_lowercase
uppers = lowers.upper ()
numbers = ''.join ([str (i) for i in range (0, 10)])
symbols = ''.join ([i for i in characters if not i in lowers+uppers+numbers])

### a function to test strength
def is_strong (pwd):

    for seq in [lowers, uppers, numbers, symbols]:
        if len ([ s for s in pwd if s in seq ])==0:
            return False

### a function to generate password
def generate_password (nchar, strength):

    bad_pwd = True
    while bad_pwd:
        password = ''.join (random.sample (characters, nchar))
        bad_pwd = is_strong (password) if strength > 6 else False
    return password

if __name__ == '__main__':

    # get users input
    text = 'From 1 (weakest) to 10 (strongest), how strong you want your password to be? '
    strength = float (raw_input (text))

    # define nchar variable
    length = int (maxchar * strength/10. + 4)
    nchar = random.randint (max (4, length-2), min (length+2, len (characters)))

    # randomly sampled password
    password = generate_password (nchar, strength)

    # print results
    print ('your password: {0}'.format (password))


