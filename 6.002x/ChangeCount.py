#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write a countChangeRec using recursion for counting the number
# of ways to make change for a given amount of money in cents
# using a given list of coin denominations list coins
# (where coins are distinct positive integers).
# For example, for coins = [1, 5, 10, 25] and amount = 15,
# there are 6 ways to make change:
# 1+1+1+1+1+10
# 1+1+1+1+5+5
# 1+1+5+5+5
# 1+1+1+1+1+1+10
# 1+1+1+1+1+5+5
# 1+5+5+5
# So countChangeRec(15, [1, 5, 10, 25]) should return 6.
# Hint: Think of the degenerate cases.
# You can use the following function to sort the coins list:
def sortCoins(coins):
    """ coins is a list of distinct positive integers """
    coins.sort()
    coins.reverse()
    return coins

def countChangeRec(amount, coins):
    """ amount is a positive integer, coins is a list of distinct positive integers """
    # base case
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if coins == []:
        return 0
    # recursive case
    return countChangeRec(amount - coins[0], coins) + countChangeRec(amount, coins[1:])

# Test cases
print(countChangeRec(15, [1, 5, 10, 25]))
print(countChangeRec(15, [1, 5, 10, 25, 50]))
print(countChangeRec(100, [1, 5, 10, 25, 50]))
print(countChangeRec(100, [1, 5, 10, 25, 50, 100]))

# Write a countChangeDP using dynamic programming for counting the number
# of ways to make change for a given amount of money in cents
# using a given list of coin denominations list coins
# (where coins are distinct positive integers).

def countChangeDP(amount, coins):
    """ amount is a positive integer, coins is a list of distinct positive integers """
    # using dynamic programming
    # initialize table
    table = [0] * (amount + 1)
    # base case
    table[0] = 1
    # recursive case
    for coin in coins:
        for i in range(coin, amount + 1):
            table[i] += table[i - coin]
    return table[amount]

# Test cases
print(countChangeDP(15, [1, 5, 10, 25]))
print(countChangeDP(15, [1, 5, 10, 25, 50]))
print(countChangeDP(100, [1, 5, 10, 25, 50]))
print(countChangeDP(100, [1, 5, 10, 25, 50, 100]))
