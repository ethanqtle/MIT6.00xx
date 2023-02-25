# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:12:46 2023

@author: ethan
"""

# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception as ex:
#         print(ex)
        
# fancy_divide([0,2,4], 0)

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
fancy_divide([0, 2, 4], 0)
