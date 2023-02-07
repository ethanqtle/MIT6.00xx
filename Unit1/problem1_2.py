# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:02:21 2023

@author: ethanle
"""

s = 'azcbobobegghakl'
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

# Paste your code into this box 
numWord = 0
for i in range(len(s)-2):
    if s[i:i+3] == "bob":
        numWord += 1
print('Number of times bob occurs is:',numWord)