from cProfile import run
from calendar import c
import os
import string
import numpy as np

#f = open("2022/input-10-test", "r")
#f = open("2022/input-10", "r")
f = open("2022/input-10-test1", "r")

allLst = f.read().splitlines()

#print (allLst)

cycCnt = 1
#instBufCyc = ''
#instBufCntr = 0
instBuf = []
x = 1
bigAddr = 0

litArr = np.zeros((6,40), dtype=int)

print (litArr)

# part 1
"""
lst_of_ints = [[20,0],  [60,0],  [100,0], [140,0], [180,0], [220,0]]

for itms in allLst:
    #print (x, cycCnt)
    if (itms.split()[0]=='addx'):
        for mrkrs in lst_of_ints:
            if mrkrs[1] == 0:
                if (cycCnt == mrkrs[0]) or (cycCnt + 1 == mrkrs[0]):
                    #print (mrkrs[0], x, cycCnt)
                    bigAddr = bigAddr + mrkrs[0]*x
                    mrkrs[1] = 1
        cycCnt = cycCnt + 2
        x = x + int(itms.split()[1])
        #print ("after add: ", x , cycCnt)

    elif (itms == 'noop'):
        for mrkrs in lst_of_ints:
            if mrkrs[1] == 0:
                if (cycCnt == mrkrs[0]) or (cycCnt + 1 == mrkrs[0]):
                    #print (mrkrs[0], x, cycCnt)
                    bigAddr = bigAddr + mrkrs[0]*x
                    mrkrs[1] = 1
        cycCnt = cycCnt +1
        #print ("after noop: ", x , cycCnt)

print (bigAddr)
print (x, cycCnt)
"""


#part 2



for itms in allLst:
    #print (x, cycCnt)
    if cycCnt in ([x-1, x, x+1]):
        xRow = cycCnt %
    if (itms.split()[0]=='addx'):
        cycCnt = cycCnt + 2
        x = x + int(itms.split()[1])
        #print ("after add: ", x , cycCnt)


    elif (itms == 'noop'):
        cycCnt = cycCnt +1
        #print ("after noop: ", x , cycCnt)