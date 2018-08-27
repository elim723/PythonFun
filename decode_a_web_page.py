#!/usr/bin/env python

# import
import requests
from bs4 import BeautifulSoup

# define variables
url = 'https://www.nytimes.com/'
r = requests.get (url)
soup = BeautifulSoup (r.text, 'html.parser')

# get titles
titles = soup.find_all ('h2')

# print
for n in range (len (titles)):
    title = titles [n].contents[0].encode ('utf-8').strip ()
    print ('{0} {1}'.format (n, title))
