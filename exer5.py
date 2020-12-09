import os
import itertools
import re
import numpy as np

f = open("input5.txt", "r")

#remove new line chars
temp = f.read().split("\n")

sample = temp[0]
#FBFBBFF RLR
print (sample)

binInp = "0101100"
binInp2 = "101"

print (int(binInp, 2), int(binInp2, 2))
seatDct = {}

#print (len(temp), temp[0:10], type(temp))

smallLst = temp[0:10]
seatDct = {}
for idx,items in enumerate(temp):
    #print ("working on : ", items, " now")
    modStr1 = items.replace('F', '0')
    modStr2 = modStr1.replace('B', '1')
    modStr3 = modStr2.replace('R', '1')
    modStr4 = modStr3.replace('L', '0')
    #print (modStr4, int(modStr4[0:7], 2), int(modStr4[-3:],2))
    try:
        seatDct[idx] = (int(modStr4[0:7], 2), int(modStr4[-3:],2))
    except:
        print ('error at ', items)
        continue

sIdDct = {}
for key, val in seatDct.items():
    seatID = val[0]*8 + val[1]
    sIdDct[key] = seatID

import operator
maxIdx = max(sIdDct.items(), key=operator.itemgetter(1))[0]
print (max(sIdDct.items(), key=operator.itemgetter(1))[0])
print (sIdDct[maxIdx])


#part 2

seatIDLst = list(sIdDct.values())
print(sorted(seatIDLst))