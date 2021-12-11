import os
import numpy as np
import re
import string
from itertools import cycle, repeat
import collections

#f = open("input-11-test", "r")
#f = open("input-11-test1", "r")
f = open("input-11", "r")

bigLst = f.read().splitlines()
totRows = len(bigLst)
totCols = len(bigLst[0])

htArr = np.zeros((totRows, totCols), dtype=int)

for i, itms in enumerate(bigLst):
    for j, chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

def chkForNines(inpArr, inflashed=[]):
    global flashCtr
    secArr = inpArr.copy()
    noNines = 1
    incrmntArr = secArr.copy()

    for roIdx in range(0, incrmntArr.shape[0]):
        for coIdx in range(0, incrmntArr.shape[1]):
            if incrmntArr[roIdx][coIdx] > 9:
                noNines = 0

    if noNines == 1:
        print("Step done and total flashes are:  ", len(inflashed))
        return incrmntArr

    elif noNines == 0:
        for cRows in range(0, incrmntArr.shape[0]):
            for cCols in range(0, incrmntArr.shape[1]):
                if (incrmntArr[cRows][cCols] > 9):
                    incrmntArr[cRows][cCols] = 0
                    inflashed.append((cRows, cCols))
                    flashCtr += 1
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            nRow = cRows + i
                            nCol = cCols + j
                            if (nRow >= 0) & (nRow < incrmntArr.shape[0]) & (nCol >= 0) & (nCol < incrmntArr.shape[1]):
                                if incrmntArr[nRow][nCol] <= 9 and (nRow, nCol) not in inflashed:
                                    incrmntArr[nRow][nCol] += 1

        return chkForNines(incrmntArr, inflashed)

    else:
        print("Step done and here's the array ", inflashed)
        return incrmntArr


xamArr = htArr.copy()
flashCtr = 0

# part 1 below
""" for i in range(0,195):
    #print ("incoming array is: ", examArr)
    # add 1 to all
    addedArr = examArr + 1
    newArr = chkForNines(addedArr, [])
    #pass
    examArr = newArr.copy() """

# part 2

for i in range(0, 1000):
    #print ("incoming array is: ", examArr)
    # add 1 to all
    addedArr = examArr + 1
    newArr = chkForNines(addedArr, [])
    # pass
    examArr = newArr.copy()
    if (np.sum(examArr) == 0):
        break

print(i)
