# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:12:20 2023

@author: ethan
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    newHand = hand.copy()
    for letter in word:
        if letter in newHand and newHand[letter] > 0:
            newHand[letter] -= 1
        else:
            return False
    return True
