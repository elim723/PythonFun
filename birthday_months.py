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

# function to get counts
def get_counts (dictionary):

    counts = {}
    for name, date in dictionary.iteritems ():
        month = date['month']
        if month in counts:
            counts[month] += 1
        else:
            counts[month] = 1
    return counts

# function to print result
def print_result  (counts):

    ckeys = sorted (counts, key=lambda k: counts[k], reverse=True)
    for month in ckeys:
        print ('{0:2}: {1:2}'.format (month, counts[month]))

if __name__ == '__main__':

    # get dictionary
    dictionary = get_dict ()

    # count months
    counts = get_counts (dictionary)

    # print result
    print_result (counts)


