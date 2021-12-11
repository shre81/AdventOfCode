import os
import numpy as np

#f = open("input-11-test", "r")
#f = open("input-11-test1", "r")
f = open("input-11", "r")

bigLst = f.read().splitlines()
totRows = len(bigLst)
totCols = len(bigLst[0])

htArr = np.zeros((totRows, totCols), dtype=int)

# making a numpy array of what we get
for i, itms in enumerate(bigLst):
    for j, chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

def chkForNines(inpArr, inflashed=[]):
    global flashCtr
    secArr = inpArr.copy()
    noNines = 1
    incrmntArr = secArr.copy()

    # check if we have octpuses ready to flash
    for roIdx in range(0, incrmntArr.shape[0]):
        for coIdx in range(0, incrmntArr.shape[1]):
            if incrmntArr[roIdx][coIdx] > 9:
                noNines = 0
    
    # if none, done with the recursion
    if noNines == 1:
        #print("Step done and total flashes are:  ", len(inflashed))
        return incrmntArr

    elif noNines == 0:
        for cRows in range(0, incrmntArr.shape[0]):
            for cCols in range(0, incrmntArr.shape[1]):
                if (incrmntArr[cRows][cCols] > 9):
                    incrmntArr[cRows][cCols] = 0
                    inflashed.append((cRows, cCols)) # keep a track of what's been flashed in this step
                    flashCtr += 1 # and their count
                    # check adjacents
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            nRow = cRows + i
                            nCol = cCols + j
                            if (nRow >= 0) & (nRow < incrmntArr.shape[0]) & (nCol >= 0) & (nCol < incrmntArr.shape[1]):
                                if incrmntArr[nRow][nCol] <= 9 and (nRow, nCol) not in inflashed: # increment them if they have not flashed
                                    incrmntArr[nRow][nCol] += 1
        # keep doing this until there are no more flashes possible, pass the list of flashed to avoid "double flashes"
        return chkForNines(incrmntArr, inflashed)


examArr = htArr.copy()
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
