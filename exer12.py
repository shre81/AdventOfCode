import os
import itertools
import re
import numpy as np
from itertools import cycle


#f = open("input12-test2.txt", "r")
f = open("input12.txt", "r")

#remove new line chars
temp = f.read().splitlines()

#print (temp)
print (len(temp))

startPos = [0,0]
startDct = {'EW': 0, 'NS': 0, 'Orient': 'E'}
wayPoint = {'EW': 10, 'NS': 1}

def orientChange(dirdeg, currOri):
    dirLst = ['E', 'N', 'W', 'S']
    dir = dirdeg[0]
    deg = int(dirdeg[1:])
    degLst = [90, 180, 270]
    dirLkup = {'L': 1, 'R': -1}
    if deg == 90:
        newOri = dirLst[(dirLst.index(currOri) + 1*dirLkup[dir]) % len(dirLst)]
    elif deg == 180:
        newOri = dirLst[(dirLst.index(currOri) + 2*dirLkup[dir]) % len(dirLst)]
    elif deg == 270:
        newOri = dirLst[(dirLst.index(currOri) + 3*dirLkup[dir]) % len(dirLst)]
    return newOri

for items in temp:
    if items[0] == 'F':
        if startDct['Orient'] == 'E':
            startDct['EW'] = startDct['EW'] + int(items[1:])
        if startDct['Orient'] == 'W':
            startDct['EW'] = startDct['EW'] - int(items[1:])
        if startDct['Orient'] == 'N':
            startDct['NS'] = startDct['NS'] + int(items[1:])
        if startDct['Orient'] == 'S':
            startDct['NS'] = startDct['NS'] - int(items[1:])
    elif items[0] == 'N':
        startDct['NS']  = startDct['NS'] + int(items[1:])
    elif items[0] == 'S':
        startDct['NS']  = startDct['NS'] - int(items[1:])
    elif items[0] == 'E':
        startDct['EW'] = startDct['EW'] + int(items[1:])
    elif items[0] == 'W':
        startDct['EW'] = startDct['EW'] - int(items[1:])
    elif items[0] in ['R', 'L']:
        startDct['Orient'] = orientChange(items, startDct['Orient'])
    
manHatdist = abs(startDct['EW']) + abs(startDct['NS'])

#print (startDct)

print (manHatdist)
        
#part 2

startPos = [0,0]
startDct = {'EW': 0, 'NS': 0, 'Orient': 'E'}
wayPoint = {'EW': 10, 'NS': 1}

def movShp(inst, dirDct, wPt):
    numPts = int(inst[1:])
    newDct = dirDct.copy()
    newDct['EW'] = dirDct['EW'] + (wPt['EW'] * numPts)
    newDct['NS'] = dirDct['NS'] + (wPt['NS'] * numPts)
    return newDct

def wpOrientChange(dirdeg, wptDct):
    dir = dirdeg[0]
    deg = int(dirdeg[1:])
    degLst = [90, 180, 270]
    dirLkup = {'L': 1, 'R': -1}
    retDct = {}
    if deg == 90:
        retDct['NS'] = 1 * dirLkup[dir] * wptDct['EW']
        retDct['EW'] = -1 * dirLkup[dir] * wptDct['NS']
    elif deg == 180:
        retDct['NS'] = -1 * wptDct['NS']
        retDct['EW'] = -1 * wptDct['EW']
    elif deg == 270:
        retDct['NS'] = -1 * dirLkup[dir]* wptDct['EW']
        retDct['EW'] = 1 * dirLkup[dir]* wptDct['NS']
    return retDct

ewdirLkup = {'E': 1, 'W': -1}
nsdirLkup = {'N': 1, 'S': -1}

for items in temp:
    if items[0] == 'F':
        startDct = movShp(items, startDct, wayPoint)
    elif items[0] in ['N', 'S']:
        wayPoint['NS']  = wayPoint['NS'] + (int(items[1:]) * nsdirLkup[items[0]])
    elif items[0] in ['E', 'W']:
        wayPoint['EW'] = wayPoint['EW'] + (int(items[1:]) * ewdirLkup[items[0]])
    elif items[0] in ['R', 'L']:
        wayPoint = wpOrientChange(items, wayPoint)
    
manHatdist = abs(startDct['EW']) + abs(startDct['NS'])

#print (startDct)

print (manHatdist)