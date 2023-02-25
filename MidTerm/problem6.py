# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:00:40 2023

@author: ethan
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    if type(t) == int:
        return t
    elif type(t) == tuple or type(t) == list:
        maxVal = None
        for i in t:
            if maxVal is None:
                maxVal = max_val(i)
            else:
                maxVal = max(max_val(i), maxVal)
        return maxVal
