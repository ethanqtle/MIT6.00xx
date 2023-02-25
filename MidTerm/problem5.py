# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:54:31 2023

@author: ethan
"""
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    newDict = {}
    for k in d:
        val = d[k]
        if val in newDict:
            newDict[val].append(k)
        else:
            newDict[val] = [k]
    for val in newDict:
        if len(newDict[val]):
            newDict[val].sort()
    return newDict
