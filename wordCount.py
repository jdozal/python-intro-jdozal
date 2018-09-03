#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:09:59 2018

@author: Jessica Dozal

"""

#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# Set variables for input and output files
inputFname=''
outputFname=''

# Handles exception when incorrect number of arguments is given 
try: 
    inputFname = sys.argv[1]
    outputFname = sys.argv[2]
except IndexError:
    print("\nCorrect usage: wordCount.py <input text file> <output file>\n")
    exit


# Check input and output files 
if not os.path.exists(inputFname):
    print ("input file %s doesn't exist! \nExiting" % inputFname)
    exit
    
# open file to read 
inFile=open(inputFname, 'r')

# create dictionary 
my_dict=dict()

def check_word(word):
    if word == '':
        return 
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
    
# Reading every line of file 
for line in inFile:
    print(re.split('\W+', line))
    for word in re.split('\W+', line):
        word=word.lower()
        check_word(word)
        
outFile = open(outputFname,'w+') 

for key in sorted(my_dict.keys()):
    newline = ("%s %s\n" % (key, my_dict[key]))
    #print(newline)
    outFile.write(newline)
    outFile.flush()