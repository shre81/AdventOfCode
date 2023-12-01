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
        print (dict(zip(unique, counts)))
        #print ('number of occupied seats is: ', dict(zip(unique, counts)))
        break
    treeArr = np.array(modArr, copy=True)
    #print (ctr, treeArr, modArr)

#Part 2
<<<<<<< HEAD

treeArr = np.array(lstofLst)

=======

treeArr = np.array(lstofLst)

>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
for ctr in range(1, 10):
    modArr = np.array(treeArr, copy=True)
    for i in range(treeArr.shape[0]):
        for j in range(treeArr.shape[1]):
<<<<<<< HEAD
            cLst = []
            rLst = []
            dLst = []
=======
            chkLst = []
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
            for chkI in range(-treeArr.shape[0], treeArr.shape[0]):
                rowI = i + chkI
                rowJ = j
                if not((rowI == i) and (rowJ == j)):
<<<<<<< HEAD
                    rLst.append((rowI, rowJ))
=======
                    chkLst.append((rowI, rowJ))
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
            for chkJ in range(-treeArr.shape[1], treeArr.shape[1]):
                colI = i
                colJ = j + chkJ
                if not((colI == i) and (colJ == j)):
<<<<<<< HEAD
                    cLst.append((colI, colJ))
=======
                    chkLst.append((colI, colJ))
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
            for chkI in range(-treeArr.shape[0], treeArr.shape[0]):
                for chkJ in range(-treeArr.shape[1], treeArr.shape[1]):
                    if (abs(chkI)==abs(chkJ)):
                        diaI = i + chkI
                        diaJ = j + chkJ
                        if not((diaI == i) and (diaJ == j)):
<<<<<<< HEAD
                            dLst.append((diaI, diaJ))
            
            if (ctr == 2) and (i==0) and (j==0):
                print (chkLst, treeArr[i,j])
            
            if (treeArr[i,j] == 0): 
                emptySeat = 1
                for items in rLst:
                    if (0 <= items[0] <= treeArr.shape[0]) and (0 <= items[1] <= treeArr.shape[1]):
                        try:
                            if (treeArr[items[0], items[1]])==1:
                                

=======
                            chkLst.append((diaI, diaJ))
            
            if ctr == 1:
                print (chkLst)
            
            if (treeArr[i,j] == 0):
                emptySeat = 1
                for items in chkLst:
                    adjI = i + items[0]
                    adjJ = j + items[1]
                    if (adjI >= 0) and (adjJ >= 0):
                        try:
                            if (treeArr[adjI,adjJ] == 1):
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
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
                for items in chkLst:
                    adjI = i + items[0]
                    adjJ = j + items[1]
<<<<<<< HEAD
                    if (0 <= adjI <= treeArr.shape[0]) and (0 <= adjJ <= treeArr.shape[1]):
=======
                    if (adjI >= 0) and (adjJ >= 0):
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
                        try:
                            if (treeArr[adjI,adjJ] == 1):
                                occSeat.append((1, adjI, adjJ))
                        except:
                            continue
                    else:
                        #print ('boundaries crossed')
                        continue
                #print (occSeat, i, j, ctr, treeArr[-1,-1])
                if (len(occSeat) >= 5):
                    modArr[i,j] = 0
    
    if ((treeArr==modArr).all()):
        print ('no more changes after loop: ', ctr)
        unique, counts = np.unique(modArr, return_counts=True)
        #print (dict(zip(unique, counts)))
        print ('number of occupied seats is: ', dict(zip(unique, counts)))
<<<<<<< HEAD
        print (modArr)
        break
    
    treeArr = np.array(modArr, copy=True)
=======
        break
    
    treeArr = np.array(modArr, copy=True)
>>>>>>> ab8338c3cfd3c85f52404e34477ac4624497e5e6
