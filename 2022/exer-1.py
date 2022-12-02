import os

#f = open("input-1-test", "r")
f = open("input-1", "r")

bigLst = []
trckDct = {}
ctr = 1
for items in f:
    if (items == "\n"):
        trckDct[ctr] = sum(bigLst) 
        ctr = ctr + 1
        bigLst = []
        continue
    else:
        bigLst.append(int(items))

trckDct[ctr] = sum(bigLst) 
print (len(bigLst))

#print (bigLst)
#print (trckDct)
maxLst = sorted(trckDct.values(), reverse=True)
print(sum(maxLst[0:3]))
#print (max(trckDct.values()))