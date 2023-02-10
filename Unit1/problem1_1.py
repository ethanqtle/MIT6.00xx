# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:56:39 2023

@author: ethanle
"""
s = 'azcbobobegghakl'
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
# if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

# Paste your code into this box 
numVowel = 0
for letter in s:
    if letter in "aeiou":
        numVowel += 1
print("Number of vowels:", numVowel)
