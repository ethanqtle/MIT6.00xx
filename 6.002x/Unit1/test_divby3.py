# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:17:26 2023

@author: ethan
"""

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
import re

def isDivisibleBy3(s):
    """
    Returns True if the binary string s is divisible by 3
    """
    # check if the string is a binary number
    if re.match(r"^(0|(1(01*0)*1))*0*$", s):
        return True
    else:
        return False

# Test isDivisibleBy3
for i in range(100):
    s = bin(i)[2:]
    # check if isDivisibleBy3 is correct
    if isDivisibleBy3(s) != (i % 3 == 0):
        print("Error with", s)
    if isDivisibleBy3(s):
        print(str(i), s , str(isDivisibleBy3(s)))

print("Finished testing isDivisibleBy3")






# for i in range(60):
#     s = bin(i)[2:]
#     if isDivisibleBy3(s):
#         print(str(i), s)
#         # print("Error with", s)
#         print("Error in ", i)
# print("Finished testing isDivisibleBy3")
