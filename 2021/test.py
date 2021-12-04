import os
import numpy as np

#f = open("input-4-test", "r")
f = open("input-4", "r")

bigLst = f.read().splitlines()

whatsHere = bigLst[0].split(',')
nbrsLst = [int(x) for x in whatsHere]

print (len(bigLst))

#print (nbrsLst)

brdDct = {}
ctr = 0
mtxArr = []

for i in range(2, len(bigLst)):
    if (bigLst[i] == ''):
        #print("found the next split at: ", i)
        #brdIntLst = [int(itms) for itms in brdLst]
        brdDct[ctr] = np.array(mtxArr)
        ctr = ctr + 1
        mtxArr = []
        continue
    else:
        tstArr = list(map(int, bigLst[i].split()))
        mtxArr.append(tstArr)
brdDct[ctr] = mtxArr

#newArr = np.array(mtxArr)
#print (brdDct[99], len(brdDct))

filDct = {}
for k,v in brdDct.items():
    filDct[k] = np.ones(np.array(v).shape, dtype=int)

#print (filDct)
arrDct = {}
for k,v in brdDct.items():
    arrDct[k] = np.array(v)

#print (np.sum(filDct[3][0,:]))

tstArr = np.array([[1, 0, 1, 0, 1], [1,1,1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 0, 1, 1]])

print (np.sum(tstArr[4,:]))