# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:11:25 2023

@author: ethan
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def poly(x):
        sumVal = 0
        powFact = 1
        ## step backward
        for i in range(len(L)-1,-1,-1):
            sumVal += L[i] * powFact
            powFact *= x
        return sumVal
    return poly

