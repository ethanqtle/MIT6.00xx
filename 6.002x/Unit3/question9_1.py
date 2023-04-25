# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:02:26 2023

@author: ethan
"""
import numpy, pylab

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        # FILL THIS IN
        # if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

highTemps, lowTemps = loadFile()

diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
pylab.plot(range(1,32), diffTemps)