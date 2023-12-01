import os
import numpy as np
from operator import itemgetter

#f = open("input-13-test", "r")
#f = open("input-13-test1", "r")
f = open("input-13", "r")

bigLst = f.read().splitlines()

fldInstr = []
coordsLst = []

for itms in bigLst:
    if itms.startswith('fo'):
        #print (itms, " is a folding instruction")
        axis = itms[11]
        pos =  int(itms[13:])
        fldInstr.append((axis,pos))
    else:
        tmpLst = itms.split(',')
        try:
            tmp2Lst = [int(x) for x in tmpLst]
        except:
            print ("unable to convert to int for: ", tmpLst)
            continue
        coordsLst.append(tmp2Lst)

print (fldInstr, len(coordsLst))

xRows = max(coordsLst, key=lambda x: x[0])[0]
yCols = max(coordsLst, key=lambda x: x[1])[1]

print (xRows, yCols)

htArr = np.zeros((xRows+1, yCols+1), dtype=int)

for itms in coordsLst:
    #print (" assigning 1 to coordinates: ", itms[0], itms[1])
    htArr[itms[0]][itms[1]] = 1

def keepFolding(arrToFold, foldPos, whtAxis='x'):
    xaxRows = arrToFold.shape[0]
    yaxCols = arrToFold.shape[1]
    #foldArr = np.zeros((xaxRows, yaxCols), dtype=int)
    if whtAxis=='y':
        if yaxCols % 2 == 0:
            yFldpnt = foldPos - 1
            foldArr = np.zeros((xaxRows, yFldpnt+1), dtype=int)
            #print ("folding rows even", yFldpnt)
            for i in range(0, yFldpnt):
                #print ("folding rows ", yFldpnt+1+i, yFldpnt-i)
                foldArr[:, yFldpnt-i] = arrToFold[:, yFldpnt+1+i] + arrToFold[:, yFldpnt-i]
        elif yaxCols % 2 == 1:
            yFldpnt = foldPos
            foldArr = np.zeros((xaxRows, yFldpnt), dtype=int)
            #print ("folding rows odd", yFldpnt)
            for i in range(1, yFldpnt+1):
                #print ("folding rows ", yFldpnt+i, yFldpnt-i)
                foldArr[:, yFldpnt-i] = arrToFold[:, yFldpnt+i] + arrToFold[:, yFldpnt-i]
    elif whtAxis == 'x':
        if xaxRows % 2 == 0:
            xFldpnt = foldPos - 1
            foldArr = np.zeros((xFldpnt+1, yaxCols), dtype=int)
            #print ("folding rows even", xFldpnt)
            for i in range(0, xFldpnt):
                #print ("folding rows even ", xFldpnt+1+i, xFldpnt-i)
                foldArr[xFldpnt-i, :] = arrToFold[xFldpnt+1+i, :] + arrToFold[xFldpnt-i, :]
        elif xaxRows % 2 == 1:
            xFldpnt = foldPos
            foldArr = np.zeros((xFldpnt, yaxCols), dtype=int)
            #print ("folding rows odd", xFldpnt)
            for i in range(1, xFldpnt+1):
                #print ("folding rows odd", xFldpnt+i, xFldpnt-i)
                foldArr[xFldpnt-i, :] = arrToFold[xFldpnt+i, :] + arrToFold[xFldpnt-i, :]
    
    return foldArr

inpArr = htArr.copy()
for itms in fldInstr:
    whcAx = itms[0]
    whcPos = itms[1]
    bckArr = keepFolding(inpArr, whcPos, whcAx)
    inpArr = bckArr.copy()

# just 1s

for rws in range(0,inpArr.shape[0]):
    for cols in range(0, inpArr.shape[1]):
        if inpArr[rws][cols] >1:
            inpArr[rws][cols] =1

print ("total ones in folded array is: ", np.sum(inpArr))
print ( "size of array is: ", inpArr.shape)

transLst = np.transpose(inpArr).tolist()

for i in transLst[:6]:
    for j in i[:40]:
        print('█' if j == 1 else ' ', end='')
    print()

