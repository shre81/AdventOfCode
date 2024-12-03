import os

f = open("input1.txt", "r")
#f = open("input1-test.txt", "r")

Lst1 = []
Lst2 = []
ctr = 0
for items in f:
    Lst1.append(int(items.split()[0]))
    Lst2.append(int(items.split()[1]))
    ctr = ctr +1

#print (Lst1)
#print (Lst2)
print (ctr)

""" mdLst1 = []
mdLst2 = []
dfLst = []

for runs in range(0,ctr):
    a = min(Lst1)
    b = min(Lst2)
    #print (a, b)
    dfLst.append(abs(a-b))
    Lst1.remove(a)
    Lst2.remove(b)
    mdLst1.append(a)
    mdLst2.append(b)

print (sum(dfLst))
 """
#part 2

strLst = []
for itms in Lst1:
    mplr = Lst2.count(itms)
    #print (mplr)
    strLst.append(mplr*itms)

#print (strLst)
print (sum(strLst))