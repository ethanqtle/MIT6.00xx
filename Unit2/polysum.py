# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:46:29 2023

@author: ethanle
"""

import math

def polysum(n, s):
    '''
    n: positive integer >= 3, the number of sides of a regular polygon
    s: positive int or float, length of each side
    
    returns: area of the polygon
    '''
    area = 0.25*n*s*s/math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter**2, 4)
