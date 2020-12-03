import os
import itertools
import re

f = open("input2.txt", "r")

bigLst = []
ctr = 0
for items in f:
    bigLst.append(items)
    ctr = ctr +1

#print (len(bigLst), ctr)

#Sample Input
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

testIdx = 1

#print (bigLst[testIdx])
test_str = '3-5 g: qhgsgpjdphghhjwqx\n'
#print ([m.start() for m in re.finditer('g', test_str)])

validPw = []
validCtr = 0

for idx, items in enumerate(bigLst):
    minCtrIdx = bigLst[idx].find('-')
    maxCtrIdx = bigLst[idx].find(' ')
    strIdx = bigLst[idx].find(':')
    minCtr = int(bigLst[idx][0:minCtrIdx])
    maxCtr = int(bigLst[idx][minCtrIdx+1:maxCtrIdx])
    strOI = bigLst[idx][strIdx+1:]
    strOI = strOI.strip(' ')
    strOI = strOI.strip('\n')
    charOI = bigLst[idx][strIdx-1:strIdx]
    charCnt = strOI.count(charOI)
    charOcc = [m.start() for m in re.finditer(charOI, strOI)]
    #charPos = strOI.find(charOI) + 1 
    charOcc = [m+1 for m in charOcc]
    if (minCtr in (charOcc)) and not(maxCtr in (charOcc)):
        #print("I am here 1")
        validPw.append((items, minCtr))
    elif not(minCtr in (charOcc)) and (maxCtr in (charOcc)):
        #print("I am here 2")
        validPw.append((items, maxCtr))

print (validPw[0:5])
print (len(validPw))