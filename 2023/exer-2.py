import os
import re

#f = open("input-2-test", "r")
f = open("input-2", "r")

maxDct = {"red": 12, "green": 13, "blue": 14}


bigLst = []
trckDct = {}
gameDct = {}
possibDct = {}
ctr = 1
for items in f:
    gams = items.split(':')
    gameDct[gams[0]] = gams[1]
    
    draws = gams[1].split(';')
    for drs in draws:
        notPossib = 0
        echDrwLst = drs.split(",")
        for echDrw in echDrwLst:
            itmsLst = echDrw.split()
            #print (itmsLst)
            matchDct = {"red": 0, "green": 0, "blue": 0}
            for legs in maxDct.keys():
                try:
                    matchDct[legs] = int(itmsLst[0])
                except:
                    print ("error converting : ", itmsLst[0])
                    continue
                for k,v in matchDct.items():
                    if v <= maxDct[k]:
                        print (k,v)
                        continue
                    else:
                        notPossib = 1
    if notPossib==0:
        possibDct[gams[0]]= int(gams[0].split()[1])


print (possibDct)       

summer = 0
for vals in possibDct.values():
    #print ("adding ", vals)
    summer = summer + vals

print (summer)

