# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:03:44 2023

@author: ethanle
"""

s = 'azcbobobegghakl'
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

# Paste your code into this box 

bestIndex  = 0
bestLength = 1
currIndex  = 0
currLength = 1
for i in range(1,len(s)):
    if s[i-1] <= s[i]:
        currLength += 1
    else:
        if currLength > bestLength:
            bestIndex = currIndex
            bestLength = currLength
        currIndex  = i
        currLength = 1
        
if currLength > bestLength:
    bestIndex = currIndex
    bestLength = currLength
print('Longest substring in alphabetical order is:', s[bestIndex:bestIndex+bestLength])
