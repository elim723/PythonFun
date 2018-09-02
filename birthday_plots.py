#!/usr/bin/env python

import os, json
import numpy as np

# import plotting stuff
import matplotlib
matplotlib.use ('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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

# months
default_months = {'1' :'Jan', '2' :'Feb', '3':'Mar', '4':'Apr', '5' :'May',
                  '6' :'Jun', '7' :'Jul', '8':'Aug', '9':'Sep', '10':'Oct',
                  '11':'Nov', '12':'Dec'}

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

    counts = {m:0 for m in default_months}
    for name, date in dictionary.iteritems ():
        counts[date['month']] += 1
    return counts

# function to formate axis
def format_axis (axis):

    # x axis
    xs = np.array (default_months.keys ()).astype (int)
    xticks = [default_months[m] for m in default_months]
    plt.xticks (xs, xticks)
    axis.tick_params (axis='x', labelsize=15)
    axis.set_xlabel ('Months', fontsize=20)

    # y axis
    axis.tick_params (axis='y', labelsize=15)
    axis.set_ylabel ('Counts', fontsize=20)
    
    # grid
    for ymaj in axis.yaxis.get_majorticklocs ():
        axis.axhline (y=ymaj, ls=':', color='gray', alpha=0.5, linewidth=0.3)
    for xmaj in axis.xaxis.get_majorticklocs ():
        axis.axvline (x=xmaj, ls=':', color='gray', alpha=0.5, linewidth=0.3)

# function to print result
def plot_result  (counts):

    h = plt.figure (figsize=(7.5, 5.5))
    gs = gridspec.GridSpec (1, 1)
    ax = h.add_subplot (gs[0])
    
    months = sorted (counts, key=lambda k: counts[k])
    xvalues = np.array (months).astype (int)
    yvalues = [counts[month] for month in months]
    print ('xvalues: {0}'.format (xvalues))
    print ('yvalues: {0}'.format (yvalues))
    ax.bar (xvalues, yvalues, width=0.6)
    format_axis (ax)

    h.savefig ('outputs/birthday_plot.pdf')
    plt.close ('all')

if __name__ == '__main__':

    # get dictionary
    dictionary = get_dict ()

    # count months
    counts = get_counts (dictionary)

    # plot result
    plot_result (counts)

