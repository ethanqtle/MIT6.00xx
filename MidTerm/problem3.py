# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:40:14 2023

@author: ethan
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    guess = 1
    diff = abs(num - guess)
    while abs(num - guess) > 0:
        guess *= base
        if diff > abs(num - guess):
            exp += 1
            diff = abs(num - guess)
        else:
            return exp
    return exp
