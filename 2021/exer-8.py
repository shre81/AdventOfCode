import os
import numpy as np

#f = open("input-8-test", "r")
f = open("input-8", "r")

bigLst = f.read().splitlines()

exam = bigLst[0].split('|')

bigDct = {}

for idx in range(0, len(bigLst)):
    spltLst = bigLst[idx].split('|')
    bigDct[idx] = (spltLst[0], spltLst[1])


somDct = {}
somDct['abc'] =1
uniqCtr = 0



def uniqNbr(someStr):
    #someStr is a list of ten strings
    
    sorStr = [''.join(sorted(i)) for i in someStr]
    returnDct = {}
    uniqDct = {2:1, 4:4, 3:7, 7:8}
    
    sixLst = []
    fifsLst = []
    
    rmvdLst = []
    for itms in sorStr:
        for keys in uniqDct.keys():
            if(len(itms) == keys):

                rmvdLst.append(itms)
                returnDct[itms] = uniqDct[keys]

    prndLst = list(set(sorStr).symmetric_difference(set(rmvdLst)))


    for itms in prndLst:    
        if (len(itms)==6):
            sixLst.append(itms)
        elif (len(itms)== 5):
            fifsLst.append(itms)

    for itms in prndLst:    
        for i in sixLst:
            #print ("checking for item: ", i)
            checker = 0
            for j in fifsLst:
                if (len(set(i).symmetric_difference(set(j))) == 1):

                    checker += 1

            if (checker == 0):
                returnDct[i] = 0
            elif (checker == 1):
                returnDct[i] = 6
            else:
                returnDct[i] = 9
        

        for j in fifsLst:
            adder = 0
            for i in sixLst:
                if (len(set(i).symmetric_difference(set(j))) == 1):
                    adder += 1

            if (adder ==1):
                returnDct[j] = 3
            elif (adder == 2):
                returnDct[j] = 5
            else:
                returnDct[j] = 2

    return returnDct

def decSum(lstOfNbrs):
    lstOfStrs = [str(i) for i in lstOfNbrs]
    stringly = ''.join(lstOfStrs)
    return int(stringly)

#print (decSum([1,1,9,7]))

sampleLst = bigDct[2][0].split()
#print (sampleLst, " is the sampel list")

nbrLst = bigDct[2][1].split()

sNbrLst = [''.join(sorted(i)) for i in nbrLst]

#print (sNbrLst)
bigAdder = 0

for k,v in bigDct.items():
    ofIntrst = v[0].split()
    nbrLst = v[1].split()
    sNbrLst = [''.join(sorted(i)) for i in nbrLst]
    disLst = []
    for itms in sNbrLst:
        disLst.append(uniqNbr(ofIntrst)[itms])
        #print (itms, uniqNbr(sampleLst)[itms])

    bigAdder += decSum(disLst)

print (bigAdder)
    