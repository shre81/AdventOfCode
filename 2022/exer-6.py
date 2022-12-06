from cProfile import run
import os
import string

#f = open("input-6-test", "r")
f = open("input-6", "r")

allLst = f.read().splitlines()

#print(len(allLst))

firstOne = allLst[0]

#print (firstOne[0])

def chkInFour(list_of_4_chars):
    fir = list_of_4_chars[0]
    sec = list_of_4_chars[1]
    thir = list_of_4_chars[2]
    if (list_of_4_chars[1:].count(fir) >= 1) or (list_of_4_chars[2:].count(sec) >= 1) or (list_of_4_chars[3:].count(thir) >= 1):
        return 0
    else:
        return 1

def chkInFourteen(list_of_14_chars):
    strtOfMsg = 0
    for idx in range(0, 14):
        coi = list_of_14_chars[idx]
        lstStrt = idx +1
        if ((list_of_14_chars[lstStrt:].count(coi)) >= 1):
            strtOfMsg = strtOfMsg + 1
    return strtOfMsg

chrsPr = 4
for idx, char in enumerate(firstOne):
    tstLst = []
    for x in range(idx, idx+4):
        tstLst.append(firstOne[x])
    #print (tstLst)
    #print (chkInFour(tstLst))
    if chkInFour(tstLst):
        #print("found a match at: ", idx)
        break
    #idx = idx + 1
    chrsPr = chrsPr + 1

#print(chrsPr)

# part 2

chrsPr2 = 14
for idx, char in enumerate(firstOne):
    tstLst = []
    for x in range(idx, idx+14):
        tstLst.append(firstOne[x])
    #print (tstLst)
    #print (chkInFour(tstLst))
    if (chkInFourteen(tstLst)==0):
        print("found a match at: ", idx)
        break
    #idx = idx + 1
    chrsPr2 = chrsPr2 + 1

print(chrsPr2)

