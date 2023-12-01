from cProfile import run
import os
import string

#f = open("input-4-test", "r")
f = open("input-4", "r")

allLst = f.read().splitlines()

bigLst = []
bigDct = {}
ctr = 0
for items in allLst:
    item1 = (items.split(',')[0]).split('-')
    item2 = (items.split(',')[1]).split('-')
    bigDct[ctr] = [item1, item2]
    ctr += 1

#print (bigDct)

def chkInside(lstOftwo):
    lowInHigh = 0
    highInLow = 0
    
    x1 = int(lstOftwo[0][0])
    x2 = int(lstOftwo[1][0])
    y1 = int(lstOftwo[0][1])
    y2 = int(lstOftwo[1][1])

    if (x1 <= x2) and (y1 >= y2):
        lowInHigh = 1
    if (x2 <= x1) and (y2 >= y1):
        highInLow = 1
    return (lowInHigh or highInLow)

totIns = 0
for k,v in bigDct.items():
    totIns = totIns + chkInside(v)

#print (totIns)

# part 2

def chkOverlap(lstOftwo):
    firstInSecond = 0
    secInFirst = 0
    
    x1 = int(lstOftwo[0][0])
    x2 = int(lstOftwo[1][0])
    y1 = int(lstOftwo[0][1])
    y2 = int(lstOftwo[1][1])

    if ( x2 <= x1 <= y2) or (x2 <= y1 <= y2):
        firstInSecond = 1
    if ( x1 <= x2 <= y1) or ( x1 <= y2 <= y1):
        secInFirst = 1

    return (firstInSecond or secInFirst)

totOvl = 0
for k,v in bigDct.items():
    totOvl = totOvl + chkOverlap(v)

print (totOvl)
