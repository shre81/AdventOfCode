import os
#from typing_extensions import final
import numpy as np
import re
import string
from itertools import cycle, repeat
import collections

#f = open("input-11-test", "r")
f = open("input-11-test1", "r")
#f = open("input-11", "r")

bigLst = f.read().splitlines()

print (len(bigLst), len(bigLst[0]))

totRows = len(bigLst)
totCols = len(bigLst[0])

htArr = np.zeros((totRows,totCols), dtype=int)

for i,itms in enumerate(bigLst):
    for j,chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

#print (htArr)

def chkForNines(inpArr, inflashed = []):
    global flashCtr
    secArr = inpArr.copy()
    #print ("incoming array is: ", secArr)
    noNines = 1
    #incrmntArr = secArr + 1
    incrmntArr = secArr.copy()

    for roIdx in range(0, incrmntArr.shape[0]):
        for coIdx in range(0, incrmntArr.shape[1]):
            if incrmntArr[roIdx][coIdx] > 9:
                noNines = 0
    
    #print ("are there are any nines: ", noNines)
    if noNines == 1:
        #incrmntArr = secArr + 1
        return secArr
    
    elif noNines == 0:
        print ("will try to flash all >9s in: ", incrmntArr)
        for cRows in range(0, incrmntArr.shape[0]):
            for cCols in range(0, incrmntArr.shape[1]):
                #print ("checking this entry: ", incrmntArr[cRows][cCols])
                if (incrmntArr[cRows][cCols] > 9):
                    print ("flashing this entry: ", incrmntArr[cRows][cCols])
                    incrmntArr[cRows][cCols] = 0
                    inflashed.append((cRows, cCols))
                    print ("after flashing now flashed is: ", (cRows, cCols), inflashed)
                    flashCtr += 1          
                    for i in [-1, 0, 1]:
                        for j in [-1,0, 1]:
                            nRow = cRows + i
                            nCol = cCols + j
                            #print ("bounds for this array: ", chkdArr.shape[0], chkdArr.shape[1])
                            print ("already flashed are: ", inflashed)
                            if (nRow >=0) & (nRow < incrmntArr.shape[0]) & (nCol >=0) & (nCol < incrmntArr.shape[1]):
                                if incrmntArr[nRow][nCol] <= 9 and (nRow, nCol) not in inflashed:
                                    print ("incrementing this value: ", incrmntArr[nRow][nCol])
                                    incrmntArr[nRow][nCol] += 1
                    
                    print ("before adj Inc", incrmntArr)
                
        print ("recursing back for :", incrmntArr, inflashed)     
        return chkForNines(incrmntArr, inflashed)
    
    else:
        #print ("Step done and here's the array ", secArr )
        return secArr

#print (incOneStp(htArr))
def adjChks(anArr, jRows, jCols):
    chkdArr = anArr.copy()
    for i in [-1, 0, 1]:
        for j in [-1,0, 1]:
            nRow = jRows + i
            nCol = jCols + j
            #print ("bounds for this array: ", chkdArr.shape[0], chkdArr.shape[1])
            if (nRow >=0) & (nRow < chkdArr.shape[0]) & (nCol >=0) & (nCol < chkdArr.shape[1]):
                if chkdArr[nRow][nCol] <= 9:
                    print ("incrementing this value: ", chkdArr[nRow][nCol])
                    chkdArr[nRow][nCol] += 1

    return chkdArr

#print (htArr)
examArr = htArr.copy()
#print (examArr)
#print (examArr)
""" 
for cRows in range(0, examArr.shape[0]):
    for cCols in range(0, examArr.shape[1]):
        examArr[cRows][cCols] += 1

print ("sending this to the func: ", examArr)
totNewArr = chkForNines(examArr) """
flashCtr = 0
#incArr = chkForNines(examArr)
#print (adjChks(incArr,1,1))

#print ("input array was: ", examArr, " and output array is: ", incArr)

"""
for cRows in range(0, totNewArr.shape[0]):
    for cCols in range(0, totNewArr.shape[1]):
        totNewArr[cRows][cCols] += 1

inc2Arr = chkForNines(totNewArr)

print ("input array was: ", totNewArr, " and output array is: ", inc2Arr) """
#print (flashCtr)

flashCtr = 0
for i in range(0,1):
    print ("incoming array is: ", examArr)
    # add 1 to all
    addedArr = examArr + 1
    newArr = chkForNines(addedArr)
    #pass
    examArr = newArr.copy()

print (flashCtr, i, examArr)
    
#print (examArr+2)












