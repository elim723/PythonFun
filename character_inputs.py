#!/usr/bin/env python

## get user's inputs
name = raw_input ('What is your name? ')
age  = raw_input ('How old are you? ')
num  = raw_input ('Give me an integer number please? ')

## calculate year to be 100 year old
today = 2018
year100 = 100-int (age) + today

## print out
line = '{0}, you will be 100 year old in {1}'
for n in range (int (num)):
    print (line.format (name, year100))
