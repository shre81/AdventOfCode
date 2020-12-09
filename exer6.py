
import os
import itertools
import re
import numpy as np

f = open("input6.txt", "r")

#remove new line chars
temp = f.read().split("\n\n")

#print (temp[6], len(temp))

sliced = temp[0:10]
strDct = {}
for idx, items in enumerate(temp):
    strLst = []
    numResp = 0
    for chars in items:
        if (chars not in strLst) and not(chars == "\n"):
            strLst.append(chars)
        if chars == "\n":
            numResp += 1
        strDct[idx] = (len(strLst), numResp)

#print (strDct)

rollingSum = 0
for k, v in strDct.items():
    rollingSum = rollingSum + v[0]

print (rollingSum)

#part 2

strDct = {}
for midx, mitems in enumerate(temp):
    someLst=mitems.splitlines()
    c = set(someLst[0])
    for idx, items in enumerate(someLst):
        if idx < (len(someLst)-1):
            t = c & set(someLst[idx+1])
            c = t
    strDct[midx] = (len(c), idx)

#print (strDct)

rollingSum2 = 0
for k,v in strDct.items():
    rollingSum2 = rollingSum2+ v[0]

print (rollingSum2)
sample = ['clfnzvjhpiybwoksxm', 'snzxvyfopbmhijl', 'nxymlhjvfzspbio']

#print (''.join(set(sample[0]).intersection(sample[1])))

c = set(sample[0])
for idx, items in enumerate(sample):
    if idx < (len(sample)-1):
        t = c & set(sample[idx+1])
        c = t
        

print (c, idx)