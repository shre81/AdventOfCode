import os
import itertools

def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG

    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b


f = open("input2.txt", "r")
#f = open("input2-test.txt", "r")
#f = open("input22-test.txt", "r")
rptDct = {}
for idx,itms in enumerate(f):
    lvl = itms.split()
    tmpLst = []
    for items in lvl:
        tmpLst.append(int(items))
        rptDct[idx] = tmpLst

print (rptDct)
print (len(rptDct.keys()))

'''
valDct = {}
for k,v in rptDct.items():
    if (v[1]>v[0]):
        isItDec = 0
    elif (v[1]<v[0]):
        isItDec = 1
    #print(notValid)
    notValid = 0
    for idx, itms in enumerate(v):
        if isItDec: 
            try:
                if ((v[idx] - v[idx+1]) <= 0) or ((v[idx] - v[idx+1]) > 3): 
                    #print ("also here")
                    notValid = 1
            except:
                break
        else:
            try:
                if ((v[idx+1] - v[idx]) <= 0) or ((v[idx+1] - v[idx]) > 3): 
                    notValid = 1
            except:
                break
        #print(notValid)


    if notValid == 0:
        #print ('here')
        valDct[k] = v

print (len(valDct.keys()))
'''

#part 2

valDct = {}

def valLstChk (v):
    notValid = 0
    
    if (v[1]>v[0]):
        isItDec = 0
    elif (v[1]<v[0]):
        isItDec = 1
    else:
        
        isItDec = -99

    tupLst = pairwise(v)

    for idx, itms in enumerate(tupLst):
        if (isItDec==1): 
            if ((itms[0]- itms[1]) <= 0) or ((itms[0]- itms[1]) > 3): 
                #print ("also here")
                notValid = 1
        elif (isItDec == 0):
            if ((itms[1] - itms[0]) <= 0) or ((itms[1] - itms[0]) > 3): 
                notValid = 1
        else:
            notValid = 1

    return notValid

for k,v in rptDct.items():
    if (valLstChk(v) == 0):
        valDct[k] = v
    else:
        for idx, ts in enumerate(v):
            #print ('removing ', ts)
            modV = v.copy()
            del modV[idx]
            #print (modV)
            if (valLstChk(modV) == 0):
                valDct[k] = modV
                break

#print (valDct)
print (len(valDct.keys()))

sample = [44, 44, 40, 39, 38, 37]
sample2 = [3 ,4 ,6, 9 ,10]
sample3 = [74, 76, 78, 79]
print (valLstChk(sample3))

#def cmpTwo (x1, x2):

#print ([n for n in pairwise(sample)])

'''
v  = pairwise(sample)
lst = list(v)

print (sample, lst)'''