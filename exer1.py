#Exercise 1 of AOC 2020

#Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

import os

f = open("input.txt", "r")

bigLst = []
ctr = 0
for items in f:
    bigLst.append(int(items))
    ctr = ctr +1

#print (len(bigLst), ctr)

copyLst = bigLst.copy()
oneMoreLst = copyLst.copy()

#print (len(bigLst), len(copyLst))

tupLst = []
for org in bigLst:
    for new in copyLst:
        for newer in oneMoreLst: #Day 2 - expand to 3 numbers that add up to 2020
            chkSum = org + new + newer 
            if chkSum == 2020:
                sumOfTwo = org * new * newer
                tupLst.append((org,new,newer)) #Day 2 - expand to 3 numbers that add up to 2020

#print (tupLst, sumOfTwo)

# a different way of doing it using itertools

import itertools

prodLst = itertools.product(bigLst, repeat=2)

for items in prodLst:
    if items == 2020:
        print (items)
