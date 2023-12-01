import os
import itertools
import re
import numpy as np

#f = open("input7.txt", "r")
#f = open("input9-test.txt", "r")
f = open("input9.txt", "r")

#remove new line chars
temp = f.read().split("\n")

mainLst = [int(x) for x in temp[:-1]]

print (len(mainLst))

for idx, items in enumerate(mainLst):
    if idx >= 25:
        preAmb = mainLst[idx-25:idx]
        pairWise = []
        for pitems in preAmb:
            for aItems in preAmb:
                if pitems != aItems:
                    pairWise.append(int(pitems)+int(aItems))
        chkLst = list(set(pairWise))
        if items not in chkLst:
            print ('After initial Preamble - not found at:', idx, items)
            break
        else:
            continue

# Part 2

numOfInt = 1930745883
#numOfInt = 127

idx = len(mainLst)
while (idx >= 0):
    #print ('at index: ', idx)
    ctr=2
    while (ctr <= len(mainLst)-1):
        
        runSum = sum(mainLst[idx-ctr:idx])
        #print ('running sum is:', runSum)
        if (runSum == numOfInt):
            print ('success! found at:', idx-ctr, idx)
            break
        else:
            ctr = ctr + 1
            continue
    idx = idx - 1

print (sum(mainLst[553:570]))

print (mainLst[553:570])

print (min(mainLst[553:570]) + max(mainLst[553:570]))