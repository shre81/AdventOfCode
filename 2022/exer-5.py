from cProfile import run
import os
import string

#f = open("input-5-test", "r")
f = open("input-5", "r")

allLst = f.read().splitlines()
ctrIdx = []

for idx,itms in enumerate(allLst):
    if itms == '':
        ctrIdx.append(allLst[idx-1])
        endsAt = idx -1
        break

lineBfr = allLst[endsAt-1]
ctrIdxLst = ctrIdx[0].split()

ctrIdxILst = []
for itms in ctrIdxLst:
    ctrIdxILst.append(int(itms))

dctIdx = 1
initDct = {}
strtr = 0
for rows in ctrIdxILst:
    initDct[rows] = []
    for idx, itms in enumerate(allLst[:endsAt]):
        #print (rows)
        itmOfInt = itms[strtr+1:strtr+2]
        if itmOfInt is ' ':
            pass
            #initDct[rows].append(str('-99'))
        else:
            initDct[rows].append(itmOfInt)
            #print ("found an element")
        
    strtr = strtr + 4

instrSet = allLst[endsAt+2:]

def retMovSt(str_of_inst):
    numBxs = 5
    origRow = 12
    destRow = 17
    #print (str_of_inst)
    if (str_of_inst[6] == ''):
        nBox = int(str_of_inst[5])
    else:
        nBox = int(str_of_inst[5:7])
    
    if (str_of_inst[13] == ''):
        orig = int(str_of_inst[12])
    else:
        orig = int(str_of_inst[12:14])

    if (str_of_inst[17] == ''):
        dest = int(str_of_inst[17])
    else:
        dest = int(str_of_inst[17:19])

    return ([nBox, orig, dest])

""" for items in instrSet:
    getInstr = retMovSt(items)
    for counts in range(0,getInstr[0]):
        rmvr = initDct[getInstr[1]].pop(0)
        initDct[getInstr[2]].insert(0,rmvr)

print (initDct) """
    
# part 2

chkSet = instrSet[0:2]
#print (chkSet)
origDct = dict(initDct)

for items in instrSet:
    getInstr = retMovSt(items)
    rmvr = []
    for counts in range(0,getInstr[0]):
        rmvr.append(initDct[getInstr[1]].pop(0))
    initDct[getInstr[2]].insert(0,rmvr)
    #rmvr.extend(initDct[getInstr[2]])
    initDct[getInstr[2]] = [item for rmvr in initDct[getInstr[2]] for item in rmvr]

print (initDct)

#CNSCZWLVT