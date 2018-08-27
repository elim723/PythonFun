#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

# define variables
url = 'https://www.nytimes.com/'
r = requests.get (url)
soup = BeautifulSoup (r.text, 'html.parser')

# get titles
titles = [ title.contents[0].encode ('utf-8').strip ()
           for title in soup.find_all ('h2') ]

# write to a file
outfile = '/data/i3home/elims/funstuff/outputs/write_to_a_file.txt'
with open (outfile, 'wb') as f:

    # print header
    header = 'This is the output from write_to_a_file.py. \n \n' 
    f.write (header)

    # print titles
    for title in titles: f.write (title + '\n')

f.close ()
