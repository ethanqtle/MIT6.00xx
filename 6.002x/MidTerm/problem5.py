# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:14:36 2023

@author: ethan
"""

import pylab, math

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)
 
## write a simulation function to run the simulation of a drunk walking
## in a field for a given number of steps and return the list of locations 
## the drunk has visited
def simWalks(numSteps, numTrials, dClass):
    Homer = dClass('Homer')
    origin = Location(0, 0)
    locations = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        locations.append(walkVector(f, Homer, numSteps))
    return locations

# run simWalks for 1000 steps and 10 trials for each drunk type and plot
# the results for each drunk type on a separate plot
def drunkTest(walkLengths, numTrials, dClass):
    meanDistances = []
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
    # get the x and y coordinates of the locations visited by the drunk
    # in to xVals and yVals
    xVals, yVals = [], []
    for i in range(len(distances)):
        xVals.append(distances[i][0])
        yVals.append(distances[i][1])
    
    # fix plot from (-100, -100) to (100, 100)
    pylab.xlim(-100, 100)
    pylab.ylim(-100, 100)
    # calulate mean xVals and yVals
    meanX = sum(xVals)/len(xVals)
    meanY = sum(yVals)/len(yVals)
    # plot a vertical line for the mean xVals and a horizontal line for the
    # mean yVals
    pylab.axvline(x = meanX, color = 'r', linestyle = 'solid', linewidth = 2)
    pylab.axhline(y = meanY, color = 'r', linestyle = 'solid', linewidth = 2)
    
    pylab.plot(xVals, yVals, 'r.', label = dClass.__name__)
    pylab.title('Location at End of Walks (' + str(numTrials) + ' trials)')
    pylab.xlabel('X Distance')
    pylab.ylabel('Y Distance')
    pylab.legend(loc = 'best')
    pylab.show()

# run drunkTest for each drunk type
walkLengths = (500, )
numTrials = 1000
drunkTest(walkLengths, numTrials, UsualDrunk)
drunkTest(walkLengths, numTrials, ColdDrunk)
drunkTest(walkLengths, numTrials, EDrunk)
drunkTest(walkLengths, numTrials, PhotoDrunk)
drunkTest(walkLengths, numTrials, DDrunk)

