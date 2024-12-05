import os
import itertools

#f = open("input5.txt", "r")
#f = open("input5-test1.txt", "r")
#f1 = open("input5-test2.txt", "r")

f = open("input5-1.txt", "r")
f1 = open("input5-2.txt", "r")
#f = open("input22-test.txt", "r")

rptDct = {}
for idx,itms in enumerate(f):
    lvl = itms.split()
    for items in lvl:
        #tmpLst.append(items.split('|'))
        lvl = items.split('|')
        lvl = [int(x) for x in lvl]
        rptDct[idx] = lvl

#print (rptDct)

chkDct = {}
for idx,itms in enumerate(f1):
    itms = itms.strip()
    lvl = itms.split(',')
    lvl = [int(x) for x in lvl]
    chkDct[idx] = lvl

#print (chkDct)

def ordChk(itm1, itm2, rptDct):
    ordFlag = 1
    for v in rptDct.values():
        if (v[0] == itm2) and (v[1]== itm1):
            #print ("not a match because: ", "item 1:", itm1, "item 2: ", itm2, v)
            ordFlag = 0
    return ordFlag


valDct = {}
incorrDCt = {}

for k,v in chkDct.items():
    modV = v.copy()
    allFlag = 1
    for i, val in enumerate(v):
        #print ("index is ", i)
        #print ('deleting ', v[i], " in list ", modV)
        itm1 = v[i]
        modV.remove(itm1)
       
        #modV.remove(itm1)
        #print (v, modV)
        
        for j,rems in enumerate(modV):
            #print ("sending {}, {}", itm1, modV[j])
            if ordChk(itm1, modV[j], rptDct):
                continue
            else:
                #print ("not an ordered match")
                allFlag = 0
    
    if allFlag:
        valDct[k] = v
    else:
        incorrDCt[k] = v

#print (valDct)

addr = 0
for k,v in valDct.items():
    if (len(v) %2 == 0):
        print ("found an even numbered list")
        pass
    else:
        midl = len(v)/2
        midl = midl - 0.5
        
        addr = addr + v[int(midl)]

print (addr)    

#part 2

#print (incorrDCt)

#print (list(itertools.permutations(incorrDCt[3])))

def valLstchk(v):
    modV = v.copy()
    allFlag = 1
    for i, val in enumerate(v):
        #print ("index is ", i)
        #print ('deleting ', v[i], " in list ", modV)
        itm1 = v[i]
        modV.remove(itm1)
    
        #modV.remove(itm1)
        #print (v, modV)
        
        for j,rems in enumerate(modV):
            #print ("sending {}, {}", itm1, modV[j])
            if ordChk(itm1, modV[j], rptDct):
                #print ("list in order", itm1, modV[j])
                tups = (0,0)
                continue
            else:
                #print ("not an ordered match")
                tups = (itm1, modV[j])
                allFlag = 0
                return (allFlag, tups)
    
    return (allFlag, tups)

#print (valLstchk([75, 97, 47, 61, 53]))

flgc, flgb = valLstchk([75, 97, 47, 61, 53])

#print (flgc, flgb[0], flgb[1])
corr_dct = {}
'''
for k,v in incorrDCt.items():
    #allPerms = list(itertools.permutations(v))
    allPerms = [list(t) for t in itertools.permutations(v)]
    #print (allPerms[0])
    for lsts in allPerms:
        #print ("checking for ", lsts)
        if valLstchk(lsts):
            corr_dct[k] = lsts
            break
        '''



def correcter(v):
    #corrLst = v.copy()
    #corrLst[j], corrLst[v.index(itm1)] = corrLst[v.index(itm1)], corrLst[j]
    #print ("checking for list: ", v)
    #print (valLstchk(v))
    flg, tups = valLstchk(v)
    #print (flg, tups)
    if flg:
        corr_dct[k] = v
    else:
        modLst = v.copy()
        inTups = tups
        #print ("trying to fix," , inTups)
        i = modLst.index(inTups[0])
        j = modLst.index(inTups[1])
        #print ("indices are :", i, j)
        modLst[i], modLst[j] = modLst[j], modLst[i]
        #print (" new list order is: ", modLst)
        flg1, tups1 = valLstchk(modLst)
        if flg1:
            #print ("corrected list works")
            corr_dct[k] = modLst
        else:
            correcter(modLst)

for k,v in incorrDCt.items():
    #print ("checking for list: ", v)
    correcter(v)
    

print (corr_dct)

addr1 = 0
for k,v in corr_dct.items():
    if (len(v) %2 == 0):
        print ("found an even numbered list")
        pass
    else:
        midl = len(v)/2
        midl = midl - 0.5
        addr1 = addr1 + v[int(midl)]

print (addr1)    