#!/usr/bin/env python

import os, json

# default json file
jfile = 'outputs/birthdays.json'

# initial dictionary
default_dictionary = {'albert einstein'    : {'year':'1879', 'month':'3' , 'day':'14'},
                      'stephen hawking'    : {'year':'1942', 'month':'1' , 'day':'8' },
                      'isaac newton'       : {'year':'1643', 'month':'1' , 'day':'4' },
                      'jane goodall'       : {'year':'1934', 'month':'4' , 'day':'3' },
                      'madame curie'       : {'year':'1867', 'month':'11', 'day':'7' },
                      'charles darwin'     : {'year':'1809', 'month':'2' , 'day':'12'},
                      'george carver'      : {'year':'1864', 'month':'7' , 'day':'12'},
                      'neil tyson'         : {'year':'1958', 'month':'10', 'day':'5' },
                      'nicolaus copernicus': {'year':'1473', 'month':'2' , 'day':'19'},
                      'michael faraday'    : {'year':'1791', 'month':'9' , 'day':'22'},
                      'niels bohr'         : {'year':'1885', 'month':'10', 'day':'7' } }

# function to get a birthday dictionary
def get_dict ():
    
    # open json file
    if os.path.isfile (jfile):
        with open (jfile, 'rb') as f:
            dictionary = json.load (f)
        f.close ()
    else:
        ## initial dictionary
        dictionary = default_dictionary
    return dictionary

# function to save dictionary
def save_dict (dictionary):

    # save a dictionary
    with open (jfile, 'wb') as f:
        json.dump (dictionary, f)
    f.close ()

# function to return date
def get_date (dictionary):

    try:
        # ask user for a name
        name = raw_input ('Whos birthday do you want to look up? ')
        ddict = dictionary [name.lower ()]
        string = '/'.join ([ddict['month'], ddict['day'], ddict['year']])
        print ('{0} birthday is {1}.'.format (name, string))
    except:
        print ('sorry, we dont have {0} birthday..'.format (name))

# function to add date
def add_date (dictionary):

    add = True
    while add:
        # add new birthday ?
        add = raw_input ('would you like to add a birthday to my database? ')
        add = add.lower () in ['yes', 'y']

        if add:
            name = raw_input ('What is the scientists name? ')
            if name in dictionary:
                print ('your name is already in data base.'); continue
            date = raw_input ('What is his/her birthday (MM/DD/YYYY)? ').split ('/')
            dictionary [name.lower ()] = {'year':date[2],
                                          'month':date[0],
                                          'day':date[1]}
            
    return dictionary
    
if __name__ == '__main__':

    # get dictionary
    dictionary = get_dict ()

    # print out
    print ('Welcome to the birthday dictionary.')
    print ('We know the birthdays of:')
    for name in dictionary:
        print ('   {0}'.format (name))

    # get date
    get_date (dictionary)

    # add new birthday
    dictionary = add_date (dictionary)

    # save dictionary
    save_dict (dictionary)
