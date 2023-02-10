# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:36:46 2023

@author: ethanle
"""

# Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

# Code Editor
# 1

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    resultP = 1.0
    for i in range(exp):
        resultP *= base
    return resultP
