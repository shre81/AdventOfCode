from cProfile import run
import os
import string

#f = open("2022/input-9-test", "r")
f = open("2022/input-9", "r")
#f = open("2022/input-9-test1", "r")

allLst = f.read().splitlines()

headTup = (0,0)
tailTup = (0,0)

lstOfTails = []
lstOfTails.append(tailTup)

"""
# part 1

lenAdjPar = 1

def adjLstRet(tupOfInt):
    lenAdj = 1
    lstOfAdj = []
    for i in range(-lenAdj, lenAdj+1):
        for j in range(-lenAdj, lenAdj+1):
            lstOfAdj.append((tupOfInt[0] + i, tupOfInt[1]+j))
    return lstOfAdj

def chkAdj(tup1, tup2):
    xsqPt = abs(tup2[0]-tup1[0]) ** 2
    ysqPt = abs(tup2[1]-tup1[1]) ** 2
    if (xsqPt+ysqPt > 2) & (tup2[0]==tup1[0]):
        return "MovVer"
    elif (xsqPt+ysqPt > 2) & (tup2[1]==tup1[1]):
        return "MovHor"
    elif (xsqPt+ysqPt > 2) :
        return "MovDia"
    else:
        return "StlAdj"


def newTupPos(heads, tails):
    if (heads[0]==tails[0]):
        if (heads[1]>tails[1]):
            newTails = (tails[0], tails[1]+lenAdjPar)
        elif (heads[1]<tails[1]):
            newTails = (tails[0], tails[1]-lenAdjPar)
    elif (heads[1] == tails[1]):
        if (heads[0]>tails[0]):
            newTails = (tails[0] + lenAdjPar, tails[1])
        elif (heads[0] < tails[0]):
            newTails = (tails[0]-lenAdjPar, tails[1])
    else:
        if (heads[0]>tails[0]) & (heads[1]>tails[1]):
            # diagonal top right
            newTails = (tails[0]+lenAdjPar, tails[1]+lenAdjPar)
        elif (heads[0]<tails[0]) & (heads[1]<tails[1]):
            # diagonal bottom left
            newTails = (tails[0]-lenAdjPar, tails[1]-lenAdjPar)
        elif (heads[0] > tails[0]) & (heads[1]<tails[1]):
            # diagonal bottom right
            newTails = (tails[0] + lenAdjPar, tails[1]-lenAdjPar)
        elif (heads[0] < tails[0]) & (heads[1] > tails[1]):
            # diagonal top left
            newTails = (tails[0] - lenAdjPar, tails[1] + lenAdjPar)
    return newTails

#print (newTupPos((0,-1), (1,1)))

def posIntptr(curHd, aTup, numStps):
    if curHd == 'R':
        mvr = +1
        return (aTup[0]+ mvr*numStps, aTup[1])     
    elif curHd == 'L':
        mvr = -1
        return (aTup[0]+ mvr*numStps, aTup[1])
    elif curHd == 'U':
        mvr = +1
        return (aTup[0], mvr*numStps + aTup[1])
    elif curHd == 'D':
        mvr = -1
        return (aTup[0], mvr*numStps + aTup[1])

def tailsVis(tup_of_stps, hdTp, tlTp):
    for x in range(1, tup_of_stps[1]+1, 1):
        nHdTp = posIntptr(tup_of_stps[0], hdTp, x)
        #print ("new head pos is: ", nHdTp)
        adjLsts = adjLstRet(tlTp)
        #print ("current adj list for: ", tlTp, " is this: ", adjLsts)
        if nHdTp not in adjLsts:
            nTlTp = newTupPos(nHdTp, tlTp)
            if nTlTp not in lstOfTails:
                lstOfTails.append(nTlTp)
            #print ("new tail pos is: ", nTlTp)
            #tlTp = nTlTp
        else:
            continue

        tlTp = nTlTp
    hdTp = nHdTp
    
    return hdTp, tlTp

#print (tailsVis(('L', 3), (4,4), (4,3)))
#print (lstOfTails)

hds = (0,0)
tls = (0,0)            
for itms in allLst:
    currTup = (itms.split()[0], int(itms.split()[1]))
    #print (currTup, hds,tls)
    nhds, ntls = tailsVis(currTup, hds, tls)
    #print (nhds, ntls)
    hds = nhds
    tls = ntls

print (len(lstOfTails))

"""
# part 2

lenAdjPar = 1

def adjLstRet(tupOfInt):
    lenAdj = 1
    lstOfAdj = []
    for i in range(-lenAdj, lenAdj+1):
        for j in range(-lenAdj, lenAdj+1):
            lstOfAdj.append((tupOfInt[0] + i, tupOfInt[1]+j))
    return lstOfAdj

def newTupPos(heads, tails):
    if (heads[0]==tails[0]):
        if (heads[1]>tails[1]):
            newTails = (tails[0], tails[1]+lenAdjPar)
        elif (heads[1]<tails[1]):
            newTails = (tails[0], tails[1]-lenAdjPar)
    elif (heads[1] == tails[1]):
        if (heads[0]>tails[0]):
            newTails = (tails[0] + lenAdjPar, tails[1])
        elif (heads[0] < tails[0]):
            newTails = (tails[0]-lenAdjPar, tails[1])
    else:
        if (heads[0]>tails[0]) & (heads[1]>tails[1]):
            # diagonal top right
            newTails = (tails[0]+lenAdjPar, tails[1]+lenAdjPar)
        elif (heads[0]<tails[0]) & (heads[1]<tails[1]):
            # diagonal bottom left
            newTails = (tails[0]-lenAdjPar, tails[1]-lenAdjPar)
        elif (heads[0] > tails[0]) & (heads[1]<tails[1]):
            # diagonal bottom right
            newTails = (tails[0] + lenAdjPar, tails[1]-lenAdjPar)
        elif (heads[0] < tails[0]) & (heads[1] > tails[1]):
            # diagonal top left
            newTails = (tails[0] - lenAdjPar, tails[1] + lenAdjPar)
    return newTails

#print (newTupPos((0,-1), (1,1)))

def posIntptr(curHd, aTup, numStps):
    if curHd == 'R':
        mvr = +1
        return (aTup[0]+ mvr*numStps, aTup[1])     
    elif curHd == 'L':
        mvr = -1
        return (aTup[0]+ mvr*numStps, aTup[1])
    elif curHd == 'U':
        mvr = +1
        return (aTup[0], mvr*numStps + aTup[1])
    elif curHd == 'D':
        mvr = -1
        return (aTup[0], mvr*numStps + aTup[1])

def tailsLstVis(tup_of_stps, tlsLst):
    lstOfInt = tlsLst[:]
    #print (lstOfInt)
    for x in range(1, tup_of_stps[1]+1, 1):
        #print (lstOfInt)
        #print (tlsLst[0])
        newHdr = posIntptr(tup_of_stps[0], tlsLst[0], x)
        #print (newHdr)
        lstOfInt[0] = newHdr
        #print (lstOfInt)
        #nwLst = []
        #print (len(lstOfInt))
        for tls in range(0, len(lstOfInt)):
            currHd = lstOfInt[tls]
            #print ("curr header is: ", currHd, " and curr tail lst is: ", lstOfInt)
            try:
                currTl = lstOfInt[tls+1]
                #print ("current tail is: ", currTl, " at position: ", tls)
            except:
                #print ("reached end of list")
                break
            #nHdTp = posIntptr(tup_of_stps[0], currHd, x)
            #print ("current header at: ", tls, currHd, " and current tail at: ", tls+1, currTl )
            adjLsts = adjLstRet(currTl)
            #print ("current adj list for: ", currTl)
            if currHd not in adjLsts:
                #print (currHd, " not in adjLsts: ", adjLsts)
                nTlTp = newTupPos(currHd, currTl)
                #print ("new tail pos is: ", nTlTp)
            else:
                nTlTp = currTl
            #if not(tls == 0):
            #    lstOfInt[tls] = currHd
            
            lstOfInt[tls+1] = nTlTp
            #nwLst.append(nTlTp)

        #hdTp = nHdTp
        #lstOfInt = nwLst[:]
        #print (tlsLst)
        lstTail = lstOfInt[-1]
        if lstTail not in lstOfTails:
            lstOfTails.append(lstTail)
            #print ("new tail pos is: ", nTlTp, "and adding when we are at this move set: ", tup_of_stps)
            #tlTp = nTlTp
        else:
            continue

        #tlTp = nTlTp
    #hdTp = nHdTp
    
    return lstOfInt

lst_of_9s = [(0,0)]
for i in range(0,9):
    lst_of_9s.append((0,0))

#print (lst_of_9s)

#print (tailsLstVis(('R', 5), lst_of_9s))

ourLst = lst_of_9s[:]
for itms in allLst:
    currTup = (itms.split()[0], int(itms.split()[1]))
    #print (currTup, hds,tls)
    modLst = tailsLstVis(currTup, ourLst)
    #for kdx, knts in enumerate(lst_of_9s):
    #    curHd, curTl = tailsVis(currTup, hds, tls)
    #print (nhds, ntls)
    ourLst = modLst[:]

print (len(lstOfTails)) 
#print (lstOfTails)
