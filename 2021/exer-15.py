import os
import numpy as np
import time

#f = open("input-15-test", "r")
#f = open("input-15-test1", "r")
f = open("input-15-test2", "r")
#f = open("input-15", "r")

bigLst = f.read().splitlines()

print (bigLst)

totRows = len(bigLst)
totCols = len(bigLst[0])
htArr = np.zeros((totRows, totCols), dtype=int)

# making a numpy array of what we get
for i, itms in enumerate(bigLst):
    for j, chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

print (htArr.shape)

strtPos = (0, 0)

strtVal = htArr[0][0]
paths = []

# check right
foundEnd  = 0
seenPosns = []
seenPosns.append(strtPos)

finalPosn = (htArr.shape[0]-1, htArr.shape[1]-1)

print (finalPosn)

def genParents(endPos, pathTot = 0, pthSoFar = []):
    global recurCtr
    global glbDctPaths
    #endPos is a tuple of the form (x,y)
    
    print ("incoming pos: ", endPos, " and incoming path: ", pthSoFar)
    pthSoFar.append(endPos)
    # if incoming position is (0,0), task finished
    if endPos == (0,0):
        glbDctPaths[recurCtr] = pthSoFar
        print ("total value is: ", pathTot)
        print ("going to return this path: ", pthSoFar)
        return pathTot, pthSoFar    

    #print ("incoming path list: ", pthSoFar)
    corrLst = []
    parsLst = [(endPos[0]-1, endPos[1]), (endPos[0], endPos[1]-1)]
    print ("before removing non eligible points:" , parsLst)
    for itms in parsLst:
        if any(t < 0 for t in itms):
            continue
        else:
            corrLst.append(itms)
    
    print ("after removing non eligible points:" , list(set(corrLst)))
    bstLst = list(set(corrLst))
    #genTr = yield_nxt_itm(bstLst)

    currPath = pathTot + htArr[endPos[0]][endPos[1]] #value of current path
    #print ("total value is: ", currPath)
    #chkCoord = next(genTr)
    
    for pths in bstLst:
        #pthSoFar.append(pths)
        print ("going on the next run for this pos:", pths)
        recurCtr += 1
        return genParents(pths, currPath, pthSoFar)
        
    
    #else:
    #    return genParents(chkCoord, currPath, pthSoFar)

recurCtr=0
glbDctPaths = {}
print (genParents(finalPosn))

print(glbDctPaths)

print (recurCtr)

tstFin = (2,2)

lstOfPrnts = [(tstFin[0]-1, tstFin[1]), (tstFin[0], tstFin[1]-1)]

def spltAndRet(somPosn):
    #somPosn is a tuple of (x,y) form
    posn1 = (somPosn[0]-1, somPosn[1])
    posn2 = (somPosn[0], somPosn[1]-1)
    return posn1, posn2

diffPaths = []

while True:
    nxtPos1, nxtPos2 = spltAndRet(inpPosn)
    for eachPosn in (nxtPos1, nxtPos2):
        inpPosn = eachPosn
        nxtPos1, nxtPos2 = spltAndRet(inpPosn)
        
    

     
     do_something()
     if condition():
        break 

