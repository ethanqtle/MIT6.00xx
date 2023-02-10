# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:31:55 2023

@author: ethanle
"""
def square(x):
    return x * x

# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise (you don't need to redefine square in this box; when you call square, the grader will use our definition).

# This function takes in one number and returns one number.

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x) * square(x)
