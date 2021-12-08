import os
import numpy as np

#f = open("input-7-test", "r")
f = open("input-7", "r")

bigLst = f.read().splitlines()
whatsHere = bigLst[0].split(',')
nbrsLst = [int(x) for x in whatsHere]

chkLst = nbrsLst.copy()
movDct = {}

for i in range(0, len(nbrsLst)):
    moves = 0
    for j in range(0, len(chkLst)):
        numS = abs(chkLst[j]-i)
        sumNum = int((numS * (numS+1))/2)
        moves = moves + sumNum
    movDct[i] = moves

print (min(movDct.values()))

