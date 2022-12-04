from cProfile import run
import os
import string

#f = open("input-3-test", "r")
f = open("input-3", "r")

prioLow = list(string.ascii_lowercase)
prioHig = list(string.ascii_uppercase)
prioLowDct = {}
prioHigDct = {}

for idx,itms in enumerate(prioLow):
    prioLowDct[itms] = idx+1

for idx,itms in enumerate(prioHig):
    prioHigDct[itms] = idx+27

allDct = {}
allDct.update(prioHigDct)
allDct.update(prioLowDct)
#print (prioHigDct, prioLowDct)
#print (allDct)
allLst = f.read().splitlines()

thrsLSt = []
ctr = 0
for idx in range(0,len(allLst),3):
    sampLSt = allLst[idx:idx+3]
    thrsLSt.append(sampLSt)
    ctr += 1

#print (thrsLSt) 

def insPt(lst_of_3):
    insLst = list(set(lst_of_3[0]).intersection(lst_of_3[1]))
    #print (insLst)
    insPt2 = list(set(lst_of_3[2]).intersection(insLst))
    #print (insPt2)
    return allDct[insPt2[0]]

totSum= 0
for itms in thrsLSt:
    totSum = totSum + insPt(itms)

print (totSum)