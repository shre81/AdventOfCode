from cProfile import run
import os
import string
import numpy as np
import string

f = open("input-14-test", "r")
#f = open("input-14", "r")

allLst = f.read().splitlines()

coodDct = {}
for idx, lines in enumerate(allLst):
    linLst = lines.split('->')
    tmpLst = []
    for itms in linLst:
        samTup = (int(itms.split(',')[0]), int(itms.split(',')[1]))
        tmpLst.append(samTup)
    coodDct[idx] = tmpLst

print (coodDct)

def edgDet(dct_of_coords):
    xLst = [500]
    yLst = [0]
    for k,v in coodDct.items():
        for lsts in v:
            xLst.append(lsts[0])
            yLst.append(lsts[1])
    xLow = min(xLst)
    xHigh = max(xLst)
    yLow = min(yLst)
    yHigh = max(yLst)
    return (xLow, xHigh, yLow, yHigh)

def sandFiller(drwDct, edgTup):
    x1 = edgTup[0][0]
    x2 = edgTup[0][1]
    y1 = edgTup[1][0]
    y2 = edgTup[1][1]
    for k,v in drwDct.items():
        for lsts in v:
            lStrt = (lsts[0] - x1, lsts[1] -y1)

print (edgDet(coodDct))

x1, x2, y1, y2 = edgDet(coodDct)

xSiz = x2 - x1 + 1
ySiz = y2 - y1 + 1

firArr = np.zeros((xSiz, ySiz),dtype=int)

print (firArr)

sndStrt = (500-x1, 0-y1)

print (sndStrt)



