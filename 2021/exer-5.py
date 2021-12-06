import os
import numpy as np

#f = open("input-5-test", "r")
f = open("input-5", "r")

bigLst = f.read().splitlines()

#print (bigLst)
ctr = 0
linDct = {}

for idx, itms in enumerate(bigLst):
    smTxLsts = bigLst[idx].split('->')
    #print (smTxLsts)
    smTx3 = []
    for twos in smTxLsts:
        smTxTwos = twos.split(',')
        smTx3.append(tuple([int(d) for d in smTxTwos]))
    linDct[ctr] = smTx3
    ctr = ctr + 1

#print (linDct)

currMax = linDct[0][0][0]

for idx,(k,v) in enumerate(linDct.items()):
    for pts in range(0, len(v)):
        for coords in range(0,len(v[pts])):
            if (v[pts][coords] > currMax):
                newMax = v[pts][coords]
                currMax = newMax

fldArr = np.zeros((currMax+1, currMax+1), dtype = int)

print (fldArr.shape)
#print (fldArr[9][9])

itsALine = []
for idx,(k,v) in enumerate(linDct.items()):
    if (v[0][0] == v[1][0]) or (v[0][1] == v[1][1]):
        itsALine.append(k)

#print (len(itsALine))
#print ('some test examples of what we think is a line: ', linDct[itsALine[0]], linDct[itsALine[-1]])
print (len(linDct))

linCtr = 0
diagCtr = 0
notALine = []

for k,v in linDct.items():
    if (v[0][0] == v[1][0]):
        linCtr += 1
        #fldArr[v[0][0]][v[0][1]] += 1
        fldArr[v[1][0]][v[1][1]] += 1
        for dist in range(0, abs(v[1][1]-v[0][1])):
            if (v[1][1] > v[0][1]):
                if ((abs(v[0][1] + dist) != v[1][1])):
                    #print ('incrementing this entry: ', v[0][0], abs(v[0][1]+dist))
                    fldArr[v[0][0]][abs(v[0][1]+dist)] += 1
                else:
                    #fldArr[v[0][0]][abs(v[0][1]-dist)] += 1
                    print ("Done")
                    break
            if (v[1][1] < v[0][1]):
                if ((abs(v[0][1] - dist) != v[1][1])):
                    #print ('incrementing this entry: ', v[0][0], abs(v[0][1]-dist))
                    fldArr[v[0][0]][abs(v[0][1] - dist)] += 1
                else:
                    #fldArr[v[0][0]][abs(v[0][1]-dist)] += 1
                    print ("Done")
                    break
    elif (v[0][1] == v[1][1]):
        linCtr += 1
        #fldArr[v[0][0]][v[0][1]] += 1
        fldArr[v[1][0]][v[1][1]] += 1
        for dist in range(0, abs(v[0][0]-v[1][0])):
            if (v[1][0] > v[0][0]):
                if ((abs(v[0][0] + dist) != v[1][0])):
                    #print ('incrementing this entry: ', abs(v[0][0]+dist), v[0][1])
                    fldArr[abs(v[0][0]+dist)][v[0][1]] += 1
                else:
                    #fldArr[abs(v[0][0]-dist)][v[0][1]] += 1
                    print ("Done")
                    break
            if (v[1][0] < v[0][0]):
                if ((abs(v[0][0] - dist) != v[1][0])):
                    #print ('incrementing this entry: ', abs(v[0][0]-dist), v[0][1])
                    fldArr[abs(v[0][0]-dist)][v[0][1]] += 1
                else:
                    #fldArr[abs(v[0][0]-dist)][v[0][1]] += 1
                    print ("Done")
                    break
    elif ((v[1][0] - v[0][0]) == (v[1][1]-v[0][1])):
        #print ('incrementing this entry: ', v[1][0], v[1][1])
        fldArr[v[1][0]][v[1][1]] += 1
        #print ("found a diagonal at", k , v)
        for dist in range(0, abs(v[0][0]- v[1][0])):
            if (v[0][0] > v[1][0]):
                if ((abs(v[0][0] - dist) != v[1][0])):
                    tmpXIndx = v[0][0] - dist
                    tmpYIndx = v[0][1] - dist
                    #print ('incrementing this entry: ', tmpXIndx, tmpYIndx)
                    fldArr[tmpXIndx][tmpYIndx] += 1
                else:
                    break
            if (v[0][0] < v[1][0]):
                if ((abs(v[0][0] - dist) != v[1][0])):
                    tmpXIndx = v[0][0] + dist
                    tmpYIndx = v[0][1] + dist
                    #print ('incrementing this entry: ', tmpXIndx, tmpYIndx)
                    fldArr[tmpXIndx][tmpYIndx] += 1
                else:
                    break
    elif ((v[1][0] - v[0][0]) == -1*(v[1][1]-v[0][1])):
        #print ('incrementing this entry: ', v[1][0], v[1][1])
        fldArr[v[1][0]][v[1][1]] += 1
        #print ("found a diagonal at", k , v)
        for dist in range(0, abs(v[0][0]- v[1][0])):
            if (v[0][0] > v[1][0]):
                if ((abs(v[0][0] - dist) != v[1][0])):
                    tmpXIndx = v[0][0] - dist
                    tmpYIndx = v[0][1] + dist
                    #print ('incrementing this entry: ', tmpXIndx, tmpYIndx)
                    fldArr[tmpXIndx][tmpYIndx] += 1
                else:
                    break
            if (v[0][0] < v[1][0]):
                if ((abs(v[0][0] - dist) != v[1][0])):
                    tmpXIndx = v[0][0] + dist
                    tmpYIndx = v[0][1] - dist
                    #print ('incrementing this entry: ', tmpXIndx, tmpYIndx)
                    fldArr[tmpXIndx][tmpYIndx] += 1
                else:
                    break

danCtr = 0
addrCtr = {}
for x in range(0, fldArr.shape[0]):
    for y in range(0, fldArr.shape[1]):
        if (fldArr[x][y]>=2):
            addrCtr[danCtr] = (x,y)
            danCtr = danCtr + 1

print (danCtr)