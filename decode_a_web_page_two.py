#!/usr/bin/env python

# import 
import requests
from bs4 import BeautifulSoup

# define variables
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get (url)
soup = BeautifulSoup (r.text, 'html.parser')

# get content section
sections = soup.find_all (class_ = 'content-section')

# get each section
for section in sections:
    paragraphs = section.find_all ('p')
    # get each paragraph
    for paragraph in paragraphs:
        line = paragraph.text.encode ('utf-8')
        print ('{0}'.format (line))
