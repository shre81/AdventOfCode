import os
import itertools
import re
import numpy as np

#f = open("input7.txt", "r")
#f = open("input8-test.txt", "r")
f = open("input8.txt", "r")

#remove new line chars
temp = f.read().split("\n")

mastLst = []

for idx,items in enumerate(temp):
    try:
        p,q = items.split(' ')
        mastLst.append((p,int(q)))
    except:
        print (idx)
        print ('reached end of list')
        break

#print(mastLst[8])

vstdLst = []
acc = 0
idx = 0
while idx not in vstdLst:
    if mastLst[idx][0]=='nop':
        vstdLst.append(idx)
        idx = idx+1
    elif (mastLst[idx][0]=='acc'):
        vstdLst.append(idx)
        acc = acc+ mastLst[idx][1]
        idx = idx + 1
    elif (mastLst[idx][0]== 'jmp'):
        vstdLst.append(idx)
        idx = idx + mastLst[idx][1]

#print (acc, max(vstdLst), len(mastLst))

#Part 2

#mastLst.append(('nop',-99999))

changedLst = []
for midx,items in enumerate(mastLst):
    modLst = mastLst.copy()
    #print ('initial list is: ', modLst, len(modLst), len(mastLst))
    acc = 0
    idx = 0
    if mastLst[midx][0]=='nop':
        modLst[midx] = ('jmp', mastLst[midx][1])
    elif mastLst[midx][0]=='jmp':
        modLst[midx] = ('nop', mastLst[midx][1])
    changedLst.append(midx)
    #print (set(modLst) - set(mastLst))
    #print ('modified list is ', modLst, len(modLst))
    vstdLst = []
    
    while idx not in vstdLst:
        if (idx != len(modLst)):
            if (modLst[idx][0]=='nop'):
                vstdLst.append(idx)
                idx = idx+1
            elif (modLst[idx][0]=='acc'):
                vstdLst.append(idx)
                acc = acc+ modLst[idx][1]
                idx = idx + 1
            elif (modLst[idx][0]== 'jmp'):
                vstdLst.append(idx)
                idx = idx + modLst[idx][1]
        else:
            print ('reached end of list', acc)
            break
    else:
        #print ('looping again')
        continue