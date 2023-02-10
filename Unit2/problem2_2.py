# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 07:43:25 2023

@author: ethanle
"""

# Now write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months. By a fixed monthly 
# payment, we mean a single number which does not change each month, but 
# instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will
# pay off all debt in under 1 year, for example:

# Lowest Payment: 180 

# Test Case 1:
balance = 3329
annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

# Test Case 2:
balance = 4773
annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 440


# Paste your code into this box
def oneYearBalance(balance, aRate, montAmount):
    '''

    Parameters
    ----------
    balance : float
        beginning balance of the month.
    aRate : float [0,1.0]
        annual interest rate.
    montAmount : float
        monthly payment.

    Returns
    -------
    new balance.

    '''
    def monBalance(balance, aRate, montAmount):
        unpaid = balance - montAmount
        return unpaid + aRate/12.0*unpaid
    for month in range(12):
        balance = monBalance(balance, aRate, montAmount)
        
    return round(balance, 2)

amount = 10

while oneYearBalance(balance, annualInterestRate, amount) >= 0:
    amount += 10
print("Lowest Payment:", amount)