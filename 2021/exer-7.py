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
        numS = abs(chkLst[j]-i) #11
        #print (nbrsLst[i])
        #print (numS)

        sumNum = int((numS * (numS+1))/2) #66
        #print ("for these i and j:", i,chkLst[j], " the sum is: ", sumNum)
        moves = moves + sumNum
    movDct[i] = moves

#print (movDct)
print (min(movDct.values()))

