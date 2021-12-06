import os
import numpy as np

#f = open("input-6-test", "r")
f = open("input-6", "r")


bigLst = f.read().splitlines()
whatsHere = bigLst[0].split(',')
nbrsLst = [int(x) for x in whatsHere]

bigCount = len(nbrsLst)
countDct = {}

for i in range(0, 9):
    countDct[i] = nbrsLst.count(i)

print (countDct)

def creatNewDct(nums, oldDct):
    
    if (nums ==0):
        #print ("working on index: ", k, " and for this dict - ", oldDct[1])
        return oldDct[1]
    elif (nums ==1):
        return oldDct[2]
    elif (nums ==2):
        return oldDct[3]
    elif (nums ==3):
        return oldDct[4]
    elif (nums ==4):
        return oldDct[5]
    elif (nums ==5):
        return oldDct[6]
    elif (nums ==6):
        return (oldDct[7] + oldDct[0])
    elif (nums ==7):
        return (oldDct[8])
    elif (nums ==8):
        return (oldDct[0])

print (len(countDct.keys()))

for i in range(0,256):
    #print (countDct)
    #newBabies = countDct[0]
    #print (newBabies, " are the number of new babies to be created for iteration: ", i)
    tmpBabDct = {}
    for k in range(0, len(countDct.keys())):
        tmpBabDct[k] = creatNewDct(k, countDct)
    countDct = tmpBabDct.copy()
            
    #print ("at iteration: ", i, " count is: ", countDct)
    #print (nbrsLst)

print (sum(list(countDct.values())))


    