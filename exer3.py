import os
import itertools
import re
import numpy as np

f = open("input3.txt", "r")

#remove new line chars
temp = f.read().splitlines()

bigLst = []
ctr = 0
for items in temp:
    bigLst.append(items)
    ctr = ctr +1

#print (len(bigLst),bigLst[0])

lstofLst = []

#convert hashes and dots to 1s and 0
for idx, lines in enumerate(bigLst):
    lineLst = []
    for chars in lines:
        if chars == '.':
            lineLst.append(0)
        elif chars == '#':
            lineLst.append(1)
    lstofLst.append(lineLst)

#print (len(lstofLst), lstofLst[0:2])

treeArr = np.array(lstofLst)

#print (treeArr[0:10, 0:33], treeArr.shape)

treeArrexp = np.pad(treeArr, [(0, 0), (0, 1500)], 'wrap')

#print (treeArrexp[0:10, 32:64], treeArrexp.shape)

idx=0
i = 0
j = 0
oldI = 0
oldJ = 0

while (i <= treeArrexp.shape[0]):
#    while (j <= treeArrexp.shape[1]):
        idx += 1
        i = oldI+1 # i = 0, 1, 2,
        j = oldJ+3 # j = 0, 3, 6
        oldI = i
        oldJ = j
        #print (i, j, treeArrexp[i, j])
        try:
            treeArrexp[i,j] += 5
        except:
            #print ("reached end")
            exit

#print (treeArrexp[10,30], oldI, oldJ)

treeCnt = 0
nonTreeCnt = 0 
for i in range(treeArrexp.shape[0]):
    for j in range(treeArrexp.shape[1]):
        if treeArrexp[i,j] == 6:
            #print ("trees at:", i,j)
            treeCnt += 1
        elif treeArrexp[i,j] ==  5:
            #print ("no trees at:", i,j)
            nonTreeCnt += 1

print (treeCnt, nonTreeCnt)