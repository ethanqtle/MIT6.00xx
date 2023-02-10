# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 07:43:25 2023

@author: ethanle
"""

# Write a program to calculate the credit card balance after one year if a
# person only pays the minimum monthly payment required by the credit card 
# company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and 
# remaining balance. At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy - so print
# 
# Remaining balance: 813.41
# instead of

# Remaining balance: 813.4141998135 

balance = 42
annualInterestRate = 0.2	      
monthlyPaymentRate = 0.04
# Result Your Code Should Generate Below:
# Remaining balance: 31.38

balance = 484
annualInterestRate = 0.2	      
monthlyPaymentRate = 0.04
# Result Your Code Should Generate Below:
# Remaining balance: 361.61


# Paste your code into this box
def oneYearBalance(balance, aRate, monPayRate):
    '''

    Parameters
    ----------
    balance : float
        beginning balance of the month.
    aRate : float [0,1.0]
        annual interest rate.
    monPayRate : float
        monthly payment rate.

    Returns
    -------
    new balance.

    '''
    def monBalance(balance, aRate, monPayRate):
        unpaid = balance - balance * monPayRate
        return unpaid + aRate/12.0*unpaid
    for month in range(12):
        balance = monBalance(balance, aRate, monPayRate)
        
    return round(balance, 2)

print("Remaining balance:", oneYearBalance(balance, annualInterestRate , monthlyPaymentRate ))