import os

""" f = open("input-1-test", "r")
#f = open("input-1", "r")

bigLst = []
ctr = 0
for items in f:
    bigLst.append(int(items))
    ctr = ctr +1

print (len(bigLst))

incDecDct = {}

for idx, msrm in enumerate(bigLst):
    if idx == 0:
        continue
    elif bigLst[idx] > bigLst[idx-1]:
        incDecDct[idx] = 'Increase'
    else:
        continue

print (len(incDecDct)) """

# Part 2

import os


#f = open("input-1-test", "r")
f = open("input-1", "r")

bigLst = []
ctr = 0
for items in f:
    bigLst.append(int(items))
    ctr = ctr +1

print (len(bigLst))

lstSize = len(bigLst)
threeLst = []
for idx, itms in enumerate(bigLst):
    if (idx <= (lstSize - 3)):
        threeSum = bigLst[idx] + bigLst[idx+1] + bigLst[idx+2]
        threeLst.append(threeSum)

print(len(threeLst))
    
incDecDct = {}

for idx, msrm in enumerate(threeLst):
    if idx == 0:
        continue
    elif threeLst[idx] > threeLst[idx-1]:
        incDecDct[idx] = 'Increase'
    else:
        continue

print (len(incDecDct))


    