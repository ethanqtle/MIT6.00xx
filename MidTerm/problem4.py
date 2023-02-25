# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:50:07 2023

@author: ethan
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    retList = []
    for item in aList:
        if len(item) < 4:
            retList.append(item)
    return retList