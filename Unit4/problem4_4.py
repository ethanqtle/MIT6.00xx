# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:15:44 2023

@author: ethan
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    totalLen = 0
    for letter in hand:
        totalLen += hand[letter]
    return totalLen


