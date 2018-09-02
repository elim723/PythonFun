#!/usr/bin/env python

# define variable
dictionary = {'elim thompson' : {'year':'1989', 'month':'7' , 'day':'23'},
              'scott thompson': {'year':'1989', 'month':'9' , 'day':'21'},
              'liz friedman'  : {'year':'1987', 'month':'9' , 'day':'7' },
              'ken cheung'    : {'year':'1963', 'month':'1' , 'day':'4' },
              'eva chiu'      : {'year':'1963', 'month':'3' , 'day':'14'} }

# function to return date
def get_date (name):

    try:
        ddict = dictionary [name]
        return '/'.join ([ddict['month'], ddict['day'], ddict['year']])
    except:
        return None

if __name__ == '__main__':

    # print out
    print ('Welcome to the birthday dictionary.')
    print ('We know the birthdays of:')
    for name in dictionary:
        print ('   {0}'.format (name))
    
    # ask user for a name
    name = raw_input ('Whos birthday do you want to look up? ')
    name = name.lower ()

    # return
    string = get_date (name)
    if string:
        print ('{0} birthday is {1}.'.format (name, string))
    else:
        print ('sorry, we dont have {0} birthday..'.format (name))
