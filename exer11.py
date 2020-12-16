import os
import itertools
import re
import numpy as np

f = open("input11-test.txt", "r")
#f = open("input11.txt", "r")

#remove new line chars
temp = f.read().splitlines()

bigLst = []
ctr = 0
for items in temp:
    bigLst.append(items)
    ctr = ctr +1

#print (len(bigLst),bigLst)

lstofLst = []

#convert hashes and dots to 1s and 0
for idx, lines in enumerate(bigLst):
    lineLst = []
    for chars in lines:
        if chars == '.':
            lineLst.append(-1)
        elif chars == 'L':
            lineLst.append(0)
    lstofLst.append(lineLst)

#print (len(lstofLst), lstofLst[0:2])

treeArr = np.array(lstofLst)

#print (treeArr)

#first round
adjArr = [
        (-1,-1), #northwest
    (0,-1), #west
    (1, -1), #southwest
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0)
    ]

for ctr in range(1,1000):
    modArr = np.array(treeArr, copy=True)
    for i in range(treeArr.shape[0]):
        for j in range(treeArr.shape[1]):
            if (treeArr[i,j] == 0):
                emptySeat = 1
                for items in adjArr:
                    adjI = i + items[0]
                    adjJ = j + items[1]
                    if (adjI >= 0) and (adjJ >= 0):
                        try:
                            if (treeArr[adjI,adjJ] == 1):
                                emptySeat = 0
                        except:
                            continue
                    else:
                        #print ('boundaries crossed')
                        continue
                if (emptySeat == 1):
                    #print ('occupying this seat at: ', adjI, adjJ)
                    modArr[i,j] = 1
            if (treeArr[i,j] == 1):
                occSeat=[]
                for items in adjArr:
                    adjI = i + items[0]
                    adjJ = j + items[1]
                    if (adjI >= 0) and (adjJ >= 0):
                        try:
                            if (treeArr[adjI,adjJ] == 1):
                                occSeat.append((1, adjI, adjJ))
                        except:
                            continue
                    else:
                        #print ('boundaries crossed')
                        continue
                #print (occSeat, i, j, ctr, treeArr[-1,-1])
                if (len(occSeat) >= 4):
                    modArr[i,j] = 0
    
    if ((treeArr==modArr).all()):
        print ('no more changes after loop: ', ctr)
        unique, counts = np.unique(modArr, return_counts=True)
        #print (dict(zip(unique, counts)))
        print ('number of occupied seats is: ', dict(zip(unique, counts)))
        break
    treeArr = np.array(modArr, copy=True)
    #print (ctr, treeArr, modArr)

#Part 2