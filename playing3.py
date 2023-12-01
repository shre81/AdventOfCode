import os
import itertools
import re
import numpy as np
from itertools import cycle

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
        retDct['NS'] = -1 * wptDct['EW']
        retDct['EW'] = -1 * wptDct['NS']
    elif deg == 270:
        retDct['NS'] = -1 * dirLkup[dir]* wptDct['EW']
        retDct['EW'] = 1 * dirLkup[dir]* wptDct['NS']
    return retDct

#print (wpOrientChange('L90', {'EW':10, 'NS':4}))


def movShp(inst, dirDct, wPt):
    numPts = int(inst[1:])
    newDct = dirDct.copy()
    newDct['EW'] = dirDct['EW'] + (wPt['EW'] * numPts)
    newDct['NS'] = dirDct['NS'] + (wPt['NS'] * numPts)
    return newDct

print (movShp('F88', {'EW': 170, 'NS': 38}, {'EW':4, 'NS': -10}))