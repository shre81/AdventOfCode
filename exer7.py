import os
import itertools
import re
import numpy as np

f = open("input7.txt", "r")

#remove new line chars
temp = f.read().split("\n")

print (temp[0])

samStr = temp[0]
sliced = temp[0:10]

firSplit = samStr.split("contain")
secSplit = firSplit[1].split(",")

secSplitCln = [((items.strip(".")).replace("bags", "bag")).lstrip() for items in secSplit]

firSplitCln = (firSplit[0].strip()).replace("bags", "bag")

print (firSplitCln, secSplitCln)

mastDct = {}
for items in temp:
    firSplit = items.split("contain")
    try:
        secSplit = firSplit[1].split(",")
    except:
        print ("error at ", items)
        continue
    
    secSplitCln = [((items.strip(".")).replace("bags", "bag")).lstrip() for items in secSplit]
    firSplitCln = (firSplit[0].strip()).replace("bags", "bag")

    mastDct[firSplitCln] = secSplitCln

print (len(mastDct), len(temp), mastDct['drab maroon bag'])

firLevDct = {}
idx = 0
for k,v in mastDct.items():
    for items in v:
        if ('shiny gold bag') in items:
            #print (k)
            firLevDct[idx] = k
            idx = idx + 1

print (len(firLevDct))

secLevDct = {}
midx = 0
for v in firLevDct.values():
    for mk, mv in mastDct.items():
        for items in mv:
            if v in items:
                #print (mk)
                secLevDct[midx] = mk
                midx = midx + 1

print (len(secLevDct))

thiLevDct = {}
tidx = 0
for v in secLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                thiLevDct[tidx] = tk
                tidx = tidx + 1

print (len(thiLevDct))
#print (thiLevDct)

fouLevDct = {}
fidx = 0
for v in thiLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                fouLevDct[fidx] = tk
                fidx = fidx + 1

print (len(fouLevDct))

fivLevDct = {}
fividx = 0
for v in fouLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                fivLevDct[fividx] = tk
                fividx = fividx + 1

print (len(fivLevDct))

sixLevDct = {}
sidx = 0
for v in fivLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                sixLevDct[sidx] = tk
                sidx = sidx + 1

print (len(sixLevDct))

sevLevDct = {}
seidx = 0
for v in sixLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                sevLevDct[seidx] = tk
                seidx = seidx + 1

print (len(sevLevDct))

eigLevDct = {}
eiidx = 0
for v in sevLevDct.values():
    for tk, tv in mastDct.items():
        for items in tv:
            if v in items:
                #print (tk)
                eigLevDct[eiidx] = tk
                eiidx = eiidx + 1

print (len(eigLevDct))

chkInt = set(list(firLevDct.values())) | set(list(secLevDct.values())) | set(list(thiLevDct.values())) | set(list(fouLevDct.values())) | set(list(fivLevDct.values())) | set(list(sixLevDct.values())) | set(list(sevLevDct.values())) | set(list(eigLevDct.values())) 

print (len(chkInt))