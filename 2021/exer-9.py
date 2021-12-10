import os
import numpy as np

#f = open("input-9-test", "r")
f = open("input-9", "r")

bigLst = f.read().splitlines()

#print (bigLst)
print (len(bigLst), len(bigLst[0]))

totRows = len(bigLst)
totCols = len(bigLst[0])

htArr = np.zeros((totRows,totCols), dtype=int)

for i,itms in enumerate(bigLst):
    for j,chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

#print (htArr)

lowDct = {}
mastLst = []

#print (htArr[-1][0])
print (htArr.shape[1])
print (htArr.shape[0])
#print (htArr[0][htArr.shape[1]])


itemindex = np.where(htArr==1)

#print (itemindex)

for rows in range(0, (htArr.shape[0])):
    for cols in range(0, (htArr.shape[1])):
        ofInt = htArr[rows][cols]
        compLst = []
        if (rows -1 ) >= 0:
            lefty = htArr[rows-1][cols]
            #print (lefty, ofInt)
            if (ofInt < lefty):
                compLst.append(1)
            else:
                compLst.append(0)
        if (rows + 1) < htArr.shape[0]:
            righty = htArr[rows+1][cols]
            #print (righty, ofInt)
            if (ofInt < righty):
                compLst.append(1)
            else:
                compLst.append(0)
        if (cols-1) >= 0:
            uppy = htArr[rows][cols-1]
            #print (uppy, ofInt)
            if (ofInt < uppy):
                compLst.append(1)
            else:
                compLst.append(0)
        if (cols+1) < htArr.shape[1]:
            #print (cols +1)
            downy = htArr[rows][cols+1]
            #print (downy, ofInt)
            if (ofInt < downy):
                compLst.append(1)
            else:
                compLst.append(0)
        

        #compLst.append(lefty, righty, uppy, downy)
        #print ("for this item the complst is: ", ofInt, compLst)

        if (all(t == 1 for t in compLst)):
            mastLst.append((ofInt,1))

#print (mastLst)

adder = 0
for itms in mastLst:
    adder = adder + itms[0] + itms[1]

print (adder)

# Part 2

#print (htArr)

lowDct = {}
mastLst = []

#print (htArr[-1][0])
#print (htArr.shape[1])
#print (htArr.shape[0])

basDct = {}

for rows in range(0, (htArr.shape[0])):
    for cols in range(0, (htArr.shape[1])):
        ofInt = htArr[rows][cols]
        compLst = []
        if (rows -1 ) >= 0:
            lefty = htArr[rows-1][cols]
            #print (lefty, ofInt)
            if (ofInt < lefty):
                compLst.append(1)
            else:
                compLst.append(0)
        if (rows + 1) < htArr.shape[0]:
            righty = htArr[rows+1][cols]
            #print (righty, ofInt)
            if (ofInt < righty):
                compLst.append(1)
            else:
                compLst.append(0)
        if (cols-1) >= 0:
            uppy = htArr[rows][cols-1]
            #print (uppy, ofInt)
            if (ofInt < uppy):
                compLst.append(1)
            else:
                compLst.append(0)
        if (cols+1) < htArr.shape[1]:
            #print (cols +1)
            downy = htArr[rows][cols+1]
            #print (downy, ofInt)
            if (ofInt < downy):
                compLst.append(1)
            else:
                compLst.append(0)
        

        #compLst.append(lefty, righty, uppy, downy)
        #print ("for this item the complst is: ", ofInt, compLst)

        if (all(t == 1 for t in compLst)):
            mastLst.append((rows,cols))
            keyOfInt = str(ofInt) + str(rows) + str(cols)
            basDct[keyOfInt] = (rows,cols)

#print (mastLst)
#print (basDct)

modArr = htArr.copy()

for x in range(0, totRows):
    for y in range(0,totCols):
        if htArr[x][y] != 9:
            modArr[x][y] = -1

#print (modArr)

def floodFill(mtrx, x, y, oldChar, newChar):
    global counter
    
    totRows = mtrx.shape[0]
    totCols = mtrx.shape[1]

    if oldChar == None:
        oldChar = mtrx[x][y]
    
    if mtrx[x][y] != oldChar:
        return
    
    mtrx[x][y] = newChar
    counter += 1

    if x>0:
        floodFill(mtrx, x-1, y, oldChar, newChar)
    if y>0:
        floodFill(mtrx, x, y-1, oldChar, newChar)
    if x < totRows-1:
        floodFill(mtrx, x+1, y, oldChar, newChar)
    if y < totCols-1:
        floodFill(mtrx, x, y+1, oldChar, newChar)

fldDct = {}
for k,v in basDct.items():
    counter = 0
    floodFill(modArr, v[0], v[1], None, -2)
    fldDct[k] = counter

def topMax(lstOfVals):
    newLst = sorted(lstOfVals)
    return (newLst[-1] * newLst[-2] * newLst[-3])

print (topMax(fldDct.values()))


