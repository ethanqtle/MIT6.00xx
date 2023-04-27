# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:57:51 2023

@author: ethan
"""

Y = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
X = [ 0 ,1600 ,2500 ,3300 ,4000 ,4600 ,5100 ,5500 ,5750 ,5900 ,6000]

import pylab as plt
import numpy as np
z = np.polyfit(X, Y, 2)
zp = np.poly1d(z)
Yp = np.polyval(zp, X)

fix, ax = plt.subplots()
ax.plot(X, Y, 'rx',X, Yp, 'b-')
x = np.linspace(0,6000,30)
ax.plot(x, x, 'yo')
# ax.axxis('equal')
