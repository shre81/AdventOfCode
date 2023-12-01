import os
import itertools
import re
import numpy as np
from itertools import cycle
import math

#f = open("input13-test.txt", "r")
f = open("input13.txt", "r")
    
#remove new line chars
temp = f.read().splitlines()

hcf = temp[0]
numStr = temp[1]

numLst = numStr.split(',') 

#print (len(numLst))

numOILst = []

for items in numLst:
    try:
        #print (int(items))
        numOILst.append(int(items))
    except:
        continue

#print (numOILst)

dctOI = {}

for idx, nums in enumerate(numOILst):
    closFac = int(hcf)/int(nums)
    floorFac = math.floor(closFac)
    ceilFac = math.ceil(closFac) + 10
    dctOI[nums] = (list(range(floorFac, ceilFac, 1)), idx)


#print (closFac, dctOI)

factOI = {}
for k,v in dctOI.items():
    factOI[k] = min([((items*k)% int(hcf)) for items in v[0]])

kOI = min(factOI, key=factOI.get)

#print (kOI * factOI[kOI])  

#part 2

#f = open("input13-test.txt", "r")
f = open("input13.txt", "r")

#remove new line chars
temp = f.read().splitlines()

hcf = temp[0]
numStr = temp[1]

numLst = numStr.split(',') 

#print (len(numLst))

numOILst = []

for idx,items in enumerate(numLst):
    try:
        #print (int(items))
        numOILst.append((int(items), idx))
    except:
        continue

print (numOILst)

dctOI = {}

for nums in numOILst:
    closFac = int(hcf)/int(nums[0])
    floorFac = math.floor(closFac)
    ceilFac = math.ceil(closFac) + 10
    dctOI[nums[0]] = (list(range(floorFac, ceilFac, 1)), nums[1])

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

n = 10000000000 
# 10 ^ 10
allFoundLst = []
for i in range(1000000, n, 1):
    multi = numOILst[0][0] * i
    restOfLst = numOILst[1:]
    #print (restOfLst)
    foundLst = []
    if (i % 1000000):
        print ('Checked until: ', multi)
    for nidx, items in enumerate(restOfLst):
        #print (nidx, items)
        if (((multi + restOfLst[nidx][1]) % restOfLst[nidx][0]) == 0):
            #print ('found for pairs: ', restOfLst[nidx], multi)
            foundLst.append(1)
            #print (len(foundLst))
            if (len(foundLst) == (len(restOfLst))):
                #print ('Found pairs at: ', multi)
                allFoundLst.append(multi)
                break

print (len(allFoundLst), min(allFoundLst))