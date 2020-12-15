import os
import itertools
import re
import numpy as np

#f = open("input7.txt", "r")
#f = open("input10-test.txt", "r")
f = open("input10.txt", "r")

#remove new line chars
temp = f.read().split("\n")

mastLst = []

for idx,items in enumerate(temp):
    try:
        mastLst.append(int(items))
    except:
        print (idx)
        print ('reached end of list')
        break

maxJolt = max(mastLst)
mastLst.append(maxJolt+3)

startVolt = 0
currVolt = startVolt
oneJoltLst = []
threeJoltLst = []
idx = 0
while (idx <= len(mastLst)):
    #print (idx, currVolt)
    minLst = [currVolt+1, currVolt+2, currVolt+3]
    diffLst = []
    for items in minLst:
        for Mitems in mastLst:
            if (items == Mitems):
                diffLst.append((Mitems, (Mitems-currVolt)))
                #print (diffLst)
    if (diffLst):
        selItem = (min(diffLst, key = lambda t: t[1]))[0]
        volDiff = (min(diffLst, key = lambda t: t[1]))[1]
        #print (diffLst, selItem)
        currVolt = selItem
        if volDiff ==1:
            oneJoltLst.append(volDiff)
        elif volDiff == 3:
            threeJoltLst.append(volDiff)
    idx = idx + 1

print (len(oneJoltLst), len(threeJoltLst), len(mastLst))

print (75*33)
