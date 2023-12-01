import os
import numpy as np
import time

#f = open("input-14-test", "r")
f = open("input-14", "r")

bigLst = f.read().splitlines()

#print (bigLst)
ctr = 0
linDct = {}
strtSeq = bigLst[0]
smTx3 = []
rstOfLst = bigLst[2:]


for idx, itms in enumerate(rstOfLst):
    smTxLsts = itms.split('->')
    #print (smTxLsts)
    smTx3.append(tuple([d.strip() for d in smTxLsts]))

#since last char never changes and we need to add it to the last pairs and counters in the function
lastCharAll = strtSeq[-1]

# a template dict for storing char counts
allChrLst = []
for chrs in smTx3:
    allChrLst.append(chrs[1])

allChrSet = set(allChrLst)
allChrCtr = {}
for chrs in allChrSet:
    allChrCtr[chrs] = 0

# a template dict for storing pairs
polyCtr = {}
for polTups in smTx3:
    polyCtr[polTups[0]] = 0

def genPairs(someStr):
    # takes a string of polymer characters and gives you pairs of those in the given order
    pairsLst = []
    lkpDct = polyCtr.copy()
    lstChr = someStr[-1]
    #print (lkpDct)
    for idx, chrs in enumerate(someStr):
        try:
            strPair = someStr[idx] + someStr[idx+1]
            if strPair in lkpDct.keys():
                lkpDct[strPair] += 1
        except:
            #print ("reached end of string")
            break
    return lkpDct, lstChr

def prunPoly(incPairsDct, lookupLst):
    # to store the pairs
    strDct = polyCtr.copy()

    # to store the char count
    charDct = allChrCtr.copy()

    for pps, nums in incPairsDct.items():
        for lkps in lookupLst:
            if pps == lkps[0]:
                tmpStr = []
                nxtPair = []
                
                #appending first pair and part of input pairs for next step and for character count
                tmpStr.append(pps[0] + lkps[1])
                strForm = ''.join(tmpStr)
                if strForm in strDct.keys():
                    #strDct[strForm] += 1
                    strDct[strForm] += nums
                
                # now appending the 2nd pair and part of input pairs for next step BUT not for character count
                nxtPair.append(lkps[1] + pps[1])
                nxtPairStr = ''.join(nxtPair)
                if nxtPairStr in strDct.keys():
                    #strDct[nxtPairStr] += 1
                    strDct[nxtPairStr] += nums

                # only count characters from first pair formed
                for chrs in strForm:
                    if chrs in charDct.keys():
                        #charDct[chrs] += 1
                        charDct[chrs] += nums

    charDct[lastCharAll] += 1

    return strDct, charDct

# action starts here

# make an initial input dict
inpPairsDct, incLastChar = genPairs(strtSeq)
start_time = time.time()

for i in range(0, 40):
    #if ( i % 5 == 0):
    #    print ("at step :", i)
    opDct, chrCntr = prunPoly(inpPairsDct, smTx3)
    # pass
    inpPairsDct = opDct
    #incLastChar = chrCntr

print(chrCntr)
print("--- %s seconds ---" % (time.time() - start_time))