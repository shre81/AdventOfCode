import os
import re

#f = open("input-1-test", "r")
f = open("input-1", "r")

bigLst = []
trckDct = {}
ctr = 1
for items in f:
    bigLst.append(items)

#trckDct[ctr] = sum(bigLst) 
print (len(bigLst))
#print (bigLst)

mapDct = {}

numLtrs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for idx, val in enumerate(numLtrs):
    mapDct[idx+1] = val

#print (mapDct)

rvsMap = {}
for idx, val in mapDct.items():
    rvsMap[val] = idx

#print (rvsMap)

finDct = {}

for idx, ltrs in enumerate(bigLst):
    finDct[idx] = []
    tups = ()
    intsLst = []
    lstOfTups = []
    for indx, val in mapDct.items():
        
        if (ltrs.find(val) == -1):
            continue
        else:
            #pos = ltrs.find(val)
            posLst = [m.start() for m in re.finditer(val, ltrs)]
            #print (val)
            for posm in posLst:
                tups = (rvsMap[val], posm)
                lstOfTups.append(tups)
            #print (lstOfTups)

    finDct[idx]= lstOfTups
            

    for pos, chrs in enumerate(ltrs):
        #print (chrs)
        try: 
            int(chrs)
            #print (chrs)
            tups = (int(chrs), pos)
            finDct[idx].append(tups)
        except:
            continue
        #trckDct[idx] = intsLst

#Part 1
sumDct = {}
for idx, val in trckDct.items():
    summer = int(str(val[0]) + str(val[-1]))
    sumDct[idx] = summer

#Part 2
clnDct = {}
for k,v in finDct.items():
    minPos = 1000 #some arbitrary high number to get min
    maxPos = 0
    maxVal = ''
    minVal = ''
    for itms in v:    
        if itms[1] > maxPos :
            maxPos = itms[1]
            maxVal = itms[0]
        if itms[1] <= minPos:
            minPos = itms[1]
            minVal = itms[0]

    #print (k, minVal, maxVal)
    #print (k, minPos, maxPos)
    if minVal == '':
        clnDct[k] = int(str(maxVal)+str(maxVal))
    elif maxVal == '':
        clnDct[k] = int(str(minVal)+str(minVal))   
    else:
        clnDct[k] = int(str(minVal)+str(maxVal))



print (clnDct[996])
total = 0
for val in clnDct.values():
    total = total + val

print (total)