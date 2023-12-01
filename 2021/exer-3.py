import os

#f = open("input-3-test", "r")
f = open("input-3", "r")

bigLst = f.read().splitlines()

print (len(bigLst))
#print (bigLst)

lstOfLsts = []

ctr = 0
for i in range(0, len(bigLst[0])-1):
    tmpLst = []
    for itms in bigLst:
        try:
            tmpLst.append(itms[ctr])
        except:
            print ("error at: ", ctr, i, itms)
            continue
    lstOfLsts.append(tmpLst)
    ctr = ctr + 1   

print (lstOfLsts[0])

gamLst = []
epsLst = []

#lstOfLsts = [firstLst, scndLst, thrdLst, frthLst, fifLst]

for lsts in lstOfLsts:
    if lsts.count('1') > lsts.count('0'):
        gamLst.append(1)
        epsLst.append(0)
    else:
        gamLst.append(0)
        epsLst.append(1)

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

#print (gamLst, epsLst)

print (binatodeci(gamLst) * binatodeci(epsLst)) 

# Part - 2

#f = open("input-3-test", "r")
f = open("input-3", "r")

bigLst = f.read().splitlines()

print (len(bigLst))

def oxyChk(lstOfStrs, pos):
    lstOfLsts = []
    ctr = 0
    for i in range(0, len(lstOfStrs[0])):
        tmpLst = []
        for itms in lstOfStrs:
            try:
                tmpLst.append(itms[ctr])
            except:
                print ("error at: ", ctr, i, itms)
                continue
        lstOfLsts.append(tmpLst)
        ctr = ctr + 1
    
    if lstOfLsts[pos].count('1') >= lstOfLsts[pos].count('0'):
        idxPower = 1
    else:
        idxPower = 0

    prndLst = []

    for itms in lstOfStrs:
        if (int(itms[pos]) == idxPower ):
            prndLst.append(itms)
    return prndLst

newLst = bigLst.copy()
for i in range(0, len(bigLst[0])):
    #print (newLst)
    if (len(newLst) > 1):
        oldLst = newLst.copy()
        newLst = oxyChk(oldLst, i)
    else:
        #print ("Done! and the final list is: ", newLst)
        continue

#print (newLst)

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

oxyLst = list(newLst[0])
oxyNumLst = [int(itms) for itms in oxyLst]

#print(binatodeci(oxyNumLst))

def coChk(lstOfStrs, pos):
    lstOfLsts = []
    ctr = 0
    for i in range(0, len(lstOfStrs[0])):
        tmpLst = []
        for itms in lstOfStrs:
            try:
                tmpLst.append(itms[ctr])
            except:
                print ("error at: ", ctr, i, itms)
                continue
        lstOfLsts.append(tmpLst)
        ctr = ctr + 1
    
    if lstOfLsts[pos].count('1') < lstOfLsts[pos].count('0'):
        idxPower = 1
    else:
        idxPower = 0

    prndLst = []

    for itms in lstOfStrs:
        if (int(itms[pos]) == idxPower ):
            prndLst.append(itms)
    return prndLst

coLst = bigLst.copy()
for i in range(0, len(bigLst[0])):
    #print (coLst)
    if (len(coLst) > 1):
        oldLst = coLst.copy()
        coLst = coChk(oldLst, i)
    else:
        #print ("Done! and the final list is: ", coLst)
        continue

chkLst = list(coLst[0])
chkNumLst = [int(itms) for itms in chkLst]

#print (chkLst, chkNumLst)

#print (chkNumLst, oxyNumLst)

print (binatodeci(chkNumLst) * binatodeci(oxyNumLst))