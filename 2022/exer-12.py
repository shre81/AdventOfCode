from cProfile import run
import os
import string
import numpy as np
import string

f = open("input-12-test", "r")
#f = open("input-12", "r")

allLst = f.read().splitlines()

print (len(allLst[0]), len(allLst))

xRows = len(allLst[0])
yCols = len(allLst)

print (allLst)

initArr = np.zeros((xRows,yCols), dtype=np.int)
htArr = np.zeros((xRows,yCols), dtype=np.int)

def chrIntLkup(some_chr):
    return string.ascii_lowercase.index(some_chr)

print (chrIntLkup('z'))

for j,items in enumerate(allLst):
    for i,chrs in enumerate(items):
        if chrs == 'S':
            initArr[i][j] = -999
            htArr[i][j] = chrIntLkup('a')
        elif chrs == 'E':
            initArr[i][j] = 999
            htArr[i][j] = chrIntLkup('z')
        else:
            print (i,j)
            htArr[i][j] = chrIntLkup(chrs)

print (htArr)
print (initArr)