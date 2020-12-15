import os
import itertools
import re
import numpy as np

#f = open("input7.txt", "r")
f = open("input7-test.txt", "r")

#remove new line chars
temp = f.read().split("\n")

#print (temp[0])

samStr = temp[0]
sliced = temp[0:10]

firSplit = samStr.split("contain")
secSplit = firSplit[1].split(",")

secSplitCln = [((items.strip(".")).replace("bags", "bag")).lstrip() for items in secSplit]

firSplitCln = (firSplit[0].strip()).replace("bags", "bag")

#print (firSplitCln, secSplitCln)

mastDct = {}
for items in temp:
    firSplit = items.split("contain")
    try:
        secSplit = firSplit[1].split(",")
    except:
        #print ("error at ", items)
        continue
    
    secSplitCln = [((items.strip(".")).replace("bags", "bag")).lstrip() for items in secSplit]
    firSplitCln = (firSplit[0].strip()).replace("bags", "bag")

    mastDct[firSplitCln] = secSplitCln

#print (len(mastDct), len(temp), mastDct['drab maroon bag'])

'''
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
'''

#part 2 

firNstDct = {}
for k,v in mastDct.items():
    if ('shiny gold bag') in k:
        for items in v:
            firNstDct[items[2:]] = int(items[0:1])

print (len(firNstDct), firNstDct)

masterDct = firNstDct.copy()

secNstDct = {}
for ke, va in firNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                secNstDct[items[2:]] = int(items[0:1])
                masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(secNstDct), len(masterDct), secNstDct)

thiNstDct = {}
for ke, va in secNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                if 'no other bag' in items:
                    thiNstDct[items] = 0
                    masterDct[ke + '-' + items] = 0
                else:
                    thiNstDct[items[2:]] = int(items[0:1])
                    masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(thiNstDct), len(masterDct), thiNstDct)

fouNstDct = {}
for ke, va in thiNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                if 'no other bag' in items:
                    fouNstDct[items] = 0
                    masterDct[ke + '-' + items] = 0
                else:
                    fouNstDct[items[2:]] = int(items[0:1])
                    masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(fouNstDct), len(masterDct), fouNstDct)

fivNstDct = {}
for ke, va in fouNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                if 'no other bag' in items:
                    fivNstDct[items] = 0
                    masterDct[ke + '-' + items] = 0
                else:
                    fivNstDct[items[2:]] = int(items[0:1])
                    masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(fivNstDct), len(masterDct), fivNstDct)

sixNstDct = {}
for ke, va in fivNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                if 'no other bag' in items:
                    sixNstDct[items] = 0
                    masterDct[ke + '-' + items] = 0
                else:
                    sixNstDct[items[2:]] = int(items[0:1])
                    masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(sixNstDct), len(masterDct), sixNstDct)

sevNstDct = {}
for ke, va in sixNstDct.items():
    for k, v in mastDct.items():
        if ke in k:
            for items in v:
                if 'no other bag' in items:
                    sevNstDct[items] = 0
                    masterDct[ke + '-' + items] = 0
                else:
                    sevNstDct[items[2:]] = int(items[0:1])
                    masterDct[ke + '-' + items[2:]] = int(items[0:1])

print (len(sevNstDct), sevNstDct, len(masterDct))

#print (mastDct['drab maroon bag'])
megaDct = masterDct.copy()
teraDct = masterDct.copy()

for k, v in masterDct.items():
    for mek, mev in megaDct.items():
        try:
            if (k.split('-')[1] == mek.split('-')[0]) and not(mek.split('-')[1] == 'no other bag'):
                newKey = k + '-' + mek.split('-')[1]
                newVal = v * mev
                if newKey.split('-')[0] in firNstDct.keys():
                    #print (newKey, newVal)
                    teraDct[newKey] = newVal
            elif (k.split('-')[1] == mek.split('-')[0]) and (mek.split('-')[1] == 'no other bag'):
                newKey = k + '-' + mek.split('-')[1]
                newVal = v * 1
                if newKey.split('-')[0] in firNstDct.keys():
                    #print (newKey, newVal)
                    teraDct[newKey] = newVal
        except:
            continue
'''
for k, v in firNstDct.items():
    for ke, ve in masterDct.items():
        if k in ke:
            print (ke, ve)
'''
print ("printing master list below: ")
for k, v in teraDct.items():
    print (k,v)