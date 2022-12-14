from cProfile import run
import os
import string
import numpy as np

#f = open("input-8-test", "r")
f = open("input-8", "r")

allLst = f.read().splitlines()

#print (len(allLst[0]), len(allLst))

xRows = len(allLst[0])
yCols = len(allLst)

#print (allLst)

initArr = np.zeros((xRows,yCols), dtype=np.int)

for i,items in enumerate(allLst):
    for j,chrs in enumerate(items):
        initArr[i][j] = int(chrs)

#print (initArr)

rws = initArr.shape[0]
cls = initArr.shape[1]

print (rws,cls)

htArr = np.zeros((initArr.shape), dtype=np.int)

edgDct = {}
edgDct['top'] = initArr[0,:]
edgDct['bottom'] = initArr[rws-1, :]
edgDct['down1'] = initArr[:,0]
edgDct['down2'] = initArr[:,cls-1]

#print (edgDct)

innrArr = np.zeros((rws-2, cls-2), dtype=np.int)
evalArr = np.zeros((innrArr.shape), dtype=np.int)

print (innrArr.shape)

#print (innrArr.shape, evalArr.shape)

#print ("the last item in the orig array is: ", initArr[98,0], " and the last item in pruned array is: ", initArr[97,1])

evalDct = {}

ix=0
for i in range(1, rws-1):
    jx = 0
    for j in range(1, cls-1):
        #compare top
        notHighTop = 0
        notHighBot = 0
        notHighRgt = 0
        notHighLft = 0
        #print ("evaluating for: ", initArr[i,j], " at position ", i, j, " and top, bottom, left, right are: ", notHighTop, notHighBot, notHighLft, notHighRgt)
        
        for tops in range(i-1, -1, -1):
            #print ("comparing item at :", i, j, " with the item at: ", tops, j)
            if (initArr[i,j] <= initArr[tops, j]):
                notHighTop = 1  
        for bots in range(i+1, cls, 1):
            #print ("comparing item at :", i, j, " with the item at: ", bots, j)
            if (initArr[i,j] <= initArr[bots, j]):
                notHighBot = 1
        for lfts in range(j-1, -1, -1):
            #print ("comparing item at :", i, j, " with the item at: ", i, lfts)
            if (initArr[i,j] <= initArr[i, lfts]):
                notHighLft = 1
        for rgts in range(j+1, rws, 1):
            if (initArr[i,j] <= initArr[i, rgts]):
                notHighRgt = 1
        
        #print ("evaluating for: ", initArr[i,j], " at position ", i, j, " and top, bottom, left, right are: ", notHighTop, notHighBot, notHighLft, notHighRgt)
        #evalArr[i,j] = 0
        #evalDct[str(i) + str(j) + str(initArr[i,j])] = 0
        evalDct[(i,j)] = 0

        if (notHighTop + notHighBot + notHighLft + notHighRgt) < 4:
            #evalArr[i,j] = 1
            evalDct[(i,j)] = 1
                 

        jx = jx +1
    ix = ix +1

#print (innrArr)
#print (evalArr)

#print (evalDct)

#addr = (initArr.shape[0]-1)*(initArr.shape[1]-1)
addr = xRows + (yCols-1) + (xRows-1) + (yCols-2)

#print (addr)

#print (list(evalDct.values()).count(0))
#print (list(evalDct.values()).count(1))
#print (len(list(evalDct.values())))
#print (set(list(evalDct.values())))

for v in evalDct.values():
    addr = addr + v

print ("final addr is: ", addr)

#part 2


scrDct = {}
ix=0
for i in range(0, rws):
    jx = 0
    for j in range(0, cls):
        #compare top
        topScr = 0
        botScr = 0
        lftScr = 0
        rgtsScr = 0
        #print ("evaluating for: ", initArr[i,j], " at position ", i, j, " and top, bottom, left, right are: ", notHighTop, notHighBot, notHighLft, notHighRgt)
        
        for tops in range(i-1, -1, -1):
            #print ("comparing item at :", i, j, " with the item at: ", tops, j)
             
            if (initArr[i,j] <= initArr[tops, j]) or (tops==0):
                topScr = topScr + 1
                break
            else:
                topScr = topScr + 1
        for bots in range(i+1, cls, 1):
            #print ("comparing item at :", i, j, " with the item at: ", bots, j)
            #botScr = 0
            if (initArr[i,j] <= initArr[bots, j]) or (bots==0):
                botScr = botScr +1
                break
            else:
                botScr = botScr +1
        for lfts in range(j-1, -1, -1):
            #print ("comparing item at :", i, j, " with the item at: ", i, lfts)
            #lftScr = 0
            if (initArr[i,j] <= initArr[i, lfts]) or (lfts==0):
                lftScr = lftScr +1
                break
            else:
                lftScr = lftScr +1
        for rgts in range(j+1, rws, 1):
            #rgtsScr = 0
            if (initArr[i,j] <= initArr[i, rgts]) or (rgts==0):
                rgtsScr = rgtsScr +1
                break
            else:
                rgtsScr = rgtsScr +1
        #print ("evaluating for: ", initArr[i,j], " at position ", i, j, " and top, bottom, left, right are: ", notHighTop, notHighBot, notHighLft, notHighRgt)
        #evalArr[i,j] = 0
        #evalDct[str(i) + str(j) + str(initArr[i,j])] = 0
        scrDct[(i,j)] = (topScr*botScr*rgtsScr*lftScr)
                 

        jx = jx +1
    ix = ix +1

#print (scrDct)
print (max(scrDct.values()))