from cProfile import run
import os
import string
import numpy as np
import string

f = open("input-13-test", "r")
#f = open("input-13", "r")

allDct = {}

"""
for idx, lines in enumerate(f):
    if lines == '\n':
        continue
    else:
        allDct[idx]  = lines.split()
"""
tmpLst = []
for idx, lines in enumerate(f):
    output = lines.strip()
    if len(output):
        #allDct[idx] = eval(output)
        tmpLst.append(eval(output))
        allDct[idx] = tmpLst
    else:
        tmpLst = []
        #print (eval(output))

packets = [eval(output) for output in (line.strip() for line in f) if len(output)]
#allLst = f.read().splitlines()
#print (packets)

#print (allDct)

#print (allDct.keys())

sel_keys = [0,3,6,9,12,15,18,21]
indics = []
for i in range(1, len(sel_keys)+1):
    indics.append(i)

#print (indics)

strt_dct = {}
for idx, itms in enumerate(sel_keys):
    if itms in allDct.keys():
        strt_dct[indics[idx]] = allDct[itms]

print (strt_dct)

def cmpInt(int1, int2):
    if (int1 == int2):
        return 'same'
    elif (int1 < int2):
        return 'order'
    else:
        return 'notOrder'

def cmpLst(lst1, lst2):
    if (not(lst1)) and (not(lst2)):
        return 'both empty lists'
    elif (not(lst1)) and (lst2):
        #print ('one is an empty list')
        return 'order'
    elif (lst1) and (not(lst2)):
        #print ('one is an empty list')
        return 'notOrder'
    else:
        #print ('not empty lists')
        itrLst1 = iter(lst1)
        itrLst2 = iter(lst2)
        done_looping = False
        #print ('herer now')
        while not done_looping:
        #for (i,j) in zip(lst1, lst2):
            i = next(itrLst1, -999)
            j = next(itrLst2, -999)
            #print (i, j)
            if (i == -999) and (j != -999):
                return 'order'
                done_looping = True
            elif (i != -999) and (j == -999):
                return 'notOrder'
                done_looping = True
            elif (i == -999) and (j == -999):
                print ("both empty lists")
                done_looping = True
            else:
                #print (i, j)
                if isinstance(i, int) and isinstance(j, int):
                    #print ('both are ints', cmpInt(i, j))
                    if cmpInt(i,j) == 'same':
                        #print ('they are the same')
                        continue
                    elif cmpInt(i,j) == 'order':
                        #print ('they are in order')
                        return 'order'
                    elif cmpInt(i,j) == 'notOrder':
                        #print ('they are not in order')
                        return 'notOrder'
                    else:   
                        return 'something strange'
                elif isinstance(i, list) and isinstance(j, int):
                    #print (i, j)
                    #print ('comparing a list and integer')
                    return cmpLst(i, [j])
                elif isinstance(i, int) and isinstance(j, list):
                    #print ('comparing a list and integer')
                    return cmpLst([i], j)
                elif isinstance(i, list) and isinstance(j, list):
                    #print ('comparing a list and list')
                    if len(i) < len(j):
                        return 'order'
                    elif len(i) > len(j):
                        return 'notOrder'
                    else:
                        continue
                else:
                    return 'strange data types'

#print (cmpLst(strt_dct[5][0], strt_dct[5][1]))

for k,v in strt_dct.items():
    print (k, cmpLst(v[0], v[1]))

