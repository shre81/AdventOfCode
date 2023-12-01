from cProfile import run
import os
import string
import numpy as np
import string

#f = open("input-13-test", "r")
f = open("input-13", "r")

allDct = {}

#part1
"""
for idx, lines in enumerate(f):
    if lines == '\n':
        continue
    else:
        allDct[idx]  = lines.split()

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

print (list(allDct.keys())[-1])

#print (allDct.keys())

sel_keys = []
for sls in range(0, list(allDct.keys())[-1] +1 , 3):
    #print (sls)
    sel_keys.append(sls)

#sel_keys = [0,3,6,9,12,15,18,21]

indics = []
for i in range(1, len(sel_keys)+1):
    indics.append(i)

print (len(indics))

strt_dct = {}
for idx, itms in enumerate(sel_keys):
    if itms in allDct.keys():
        strt_dct[indics[idx]] = allDct[itms]

#print (strt_dct)
"""

def cmpInt(int1, int2):
    if (int1 == int2):
        return 'same'
    elif (int1 < int2):
        return 'order'
    else:
        return 'notOrder'

def cmpLst(lst1, lst2):
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
            return 'same'
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
                if (cmpLst(i, [j]) == 'same'):
                    continue
                else:
                    return cmpLst(i, [j])
            elif isinstance(i, int) and isinstance(j, list):
                #print ('comparing a list and integer')
                if (cmpLst([i], j) == 'same'):
                    continue
                else:
                    return (cmpLst([i], j))
            elif isinstance(i, list) and isinstance(j, list):
                #print ('comparing a list and list')
                if (cmpLst(i,j) == 'same'):
                    continue
                else:
                    return (cmpLst(i,j))
            else:
                return 'strange data types'

#print (cmpLst(strt_dct[4][0], strt_dct[4][1]))
"""
indAddr = 0
for k,v in strt_dct.items():
    rt_typ = cmpLst(v[0], v[1])
    #print (k, rt_typ)
    if (rt_typ =='order'):
        indAddr = indAddr + k

print (indAddr)
"""



# part 2

tmpLst = []
for idx, lines in enumerate(f):
    output = lines.strip()
    if len(output):
        #allDct[idx] = eval(output)
        tmpLst.append(eval(output))

#print (tmpLst)

tmpLst.append([[2]])
tmpLst.append([[6]])

tmpArr = np.array(tmpLst)

#print (tmpArr)

#for i in range(0, len(tmpArr)):
#    print (tmpArr[i])

def mybubsort(srt_arr):
    lstLen = len(srt_arr)
    print (lstLen)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, lstLen):
            if (cmpLst(srt_arr[i-1], srt_arr[i]) == 'notOrder'):
                x = srt_arr[i-1]
                srt_arr[i-1] = srt_arr[i]
                srt_arr[i] = x
                swapped = True
    return srt_arr

srtdArr = mybubsort(srt_arr=tmpArr)

#for i in range(0, len(srtdArr)):
    #print (srtdArr[i])

#print (srtdArr[6])

chkLst = list(srtdArr)

#print (chkLst)

print (chkLst.index([[2]]), chkLst.index([[6]]))

multip = (chkLst.index([[2]]) +1 ) *  (chkLst.index([[6]])+1)

print (multip)  

