import os

#f = open("input-2-test", "r")
f = open("input-2", "r")

bigDct = {}
ctr = 0
for items in f:
    twoItems = items.split()
    bigDct[ctr] = twoItems
    #bigLst.append(items)
    ctr = ctr +1

stTuple = [0,0]

for k,v in bigDct.items():
    if v[0] == 'forward':
        stTuple[0] = stTuple[0] + int(v[1])
    elif v[0] == 'up':
        stTuple[1] = stTuple[1] + (-1)*int(v[1])
    elif v[0] == 'down':
        stTuple[1] = stTuple[1] + (+1)*int(v[1])

print(stTuple[0]*stTuple[1])

#Part 2

#f = open("input-2-test", "r")
f = open("input-2", "r")

bigDct = {}
ctr = 0
for items in f:
    twoItems = items.split()
    bigDct[ctr] = twoItems
    #bigLst.append(items)
    ctr = ctr +1

stTuple = [0,0,0]

for k,v in bigDct.items():
    if v[0] == 'forward':
        stTuple[0] = stTuple[0] + int(v[1])
        stTuple[1] = stTuple[1]+ (stTuple[2] * int(v[1]))
    elif v[0] == 'up':
        stTuple[2] = stTuple[2] + (-1)*int(v[1])
    elif v[0] == 'down':
        stTuple[2] = stTuple[2] + (+1)*int(v[1])

print(stTuple[0]*stTuple[1])