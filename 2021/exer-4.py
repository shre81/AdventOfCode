import os
import numpy as np

#f = open("input-4-test", "r")
f = open("input-4", "r")

bigLst = f.read().splitlines()

whatsHere = bigLst[0].split(',')
nbrsLst = [int(x) for x in whatsHere]

#print (nbrsLst)

brdDct = {}
ctr = 0
mtxArr = []

for i in range(2, len(bigLst)):
    if (bigLst[i] == ''):
        brdDct[ctr] = np.array(mtxArr)
        ctr = ctr + 1
        mtxArr = []
        continue
    else:
        tstArr = list(map(int, bigLst[i].split()))
        mtxArr.append(tstArr)
brdDct[ctr] = mtxArr

filDct = {}
for k,v in brdDct.items():
    filDct[k] = np.ones(np.array(v).shape, dtype=int)

#print (filDct)
arrDct = {}
for k,v in brdDct.items():
    arrDct[k] = np.array(v)

#print (arrDct)

isBingo = 0

for itms in nbrsLst:
    if (isBingo == 0):
        for k, v in arrDct.items():
            for rws in range(0, v.shape[0]):
                for cols in range(0, v.shape[1]):
                    if (np.sum(filDct[k][rws,:])== 0) or (np.sum(filDct[k][:,cols])== 0):
                        #print ("bingo! at: ", itms)
                        #print (np.sum(filDct[k][rws,:]), np.sum(filDct[k][:,cols]), rws)
                        #print (filDct[k], arrDct[k])
                        isBingo = 1
                        bingNbr = itms
                        bingIdx = k
                        #print ("bingo index is: " , bingIdx)
                        #print ("Found bingo at card: ", k)
                        break
                    else:
                        if (v[rws][cols] == itms):
                            filDct[k][rws][cols] = 0
    else:
        #bingIdx = k
        #print (filDct, arrDct)
        break

rslt = 0

for rws in range(0, arrDct[bingIdx].shape[0]):
    for cols in range(0, arrDct[bingIdx].shape[1]):
        try:
            rslt = rslt + (arrDct[bingIdx][rws][cols] * filDct[bingIdx][rws][cols])
        except:
            print ("error at index: ", rws, cols)
            continue

print ("Part 1 answer is: ", rslt * bingNbr)

# Part 2

isBingo = 0

bngCtr = 0
bngDct = {}
ctr= 0
for itms in nbrsLst:
    for k, v in arrDct.items():
        for rws in range(0, v.shape[0]):
            for cols in range(0, v.shape[1]):
                if (np.sum(filDct[k][rws,:])== 0) or (np.sum(filDct[k][:,cols])== 0):
                    bingNbr = itms
                    bingIdx = k
                    if (k not in bngDct.values()):
                        bngDct[ctr] = k
                        ctr = ctr +1
                        whatItm = itms
                        stOfDct = filDct[k].copy()
                    break
                else:
                    if (v[rws][cols] == itms):
                        filDct[k][rws][cols] = 0

lstRslt = 0

for rws in range(0, arrDct[bngDct[ctr-1]].shape[0]):
    for cols in range(0, arrDct[bngDct[ctr-1]].shape[1]):
        try:
            lstRslt = lstRslt + (arrDct[bngDct[ctr-1]][rws][cols] * stOfDct[rws][cols])
        except:
            print ("error at index: ", rws, cols)
            continue

print ("Part 2 answer is: ",  lstRslt * whatItm)








