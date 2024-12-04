import re
import os

regex = r"\s*mul[(]\d{1,3},\d{1,3}[)]\s*"

#test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(111,888)mul(8,5))"
#test_str = open("input3.txt", "r")

with open('input3.txt', 'r') as file:
    test_str = file.read().rstrip()

#print (test_str)
#matches = re.finditer(regex, test_str, re.MULTILINE)


#part 1
'''
matches = re.findall(regex, test_str, re.MULTILINE)


for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


#matches_lst = [i.group(0) for i in matches]

for itms in matches:
    print (itms)

sumLst = []
for itms in matches:
    fir = itms.split('(')[1]
    sec = fir.split(')')[0]
    fn = int(sec.split(',')[0])
    sn = int(sec.split(',')[1])
    sumLst.append (fn*sn)

print (sum(sumLst))
'''

# part 2



#test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(111,888)mul(8,5))"
#test_str = open("input3.txt", "r")

def valMul(strOfTxt):
    regs = r"\s*mul[(]\d{1,3},\d{1,3}[)]\s*"
    try:
        matches = re.findall(regs, strOfTxt, re.MULTILINE)
    except:
        print ("input is not a string: ", strOfTxt)
        return
    sumLst = 0
    for itms in matches:
        fir = itms.split('(')[1]
        sec = fir.split(')')[0]
        fn = int(sec.split(',')[0])
        sn = int(sec.split(',')[1])
        print ("adding sum of multplying: ", fn, sn)
        sumLst  = sumLst + (fn*sn)
    return sumLst

with open('input3.txt', 'r') as file:
    inp_str = file.read().rstrip()

#print (inp_str)

regex = r"\s*mul[(]\d{1,3},\d{1,3}[)]\s*"
#regex1 = r"(?<=do[(][)])(.*?)(?=don't[(][)])"
regex1 = r"(?s).do\(\)(.*?)don't\(\)"
regex2 = r"(.*?)(?=don't[(][)])"

test_str = "]@;why()]&where()@select()mul(589,854)${ <-}$how()^#mul(517,928)^(%@#who()@'mul(82,659):don't()mul(670,226)when(626,911)from()&%{%where())-mul(244,869)<]mul(582,125)<mul(219,47):'!mul(95,365)select(){how()how()select()mul(273,775)[$!],?)@mul(955,698)what()where()/;mul(79,369)&?*$do()from()@mul(994,313)what()mul(603,3)'~@]'@@mul(729,217)#-/mul(561,454)!mul(588,577)^%'{mul(705,583){*;+;mul(418,129)~@:^mul(449,366)@what()},-)):^*mul(842,848)%what()where():what()))<from()/mul(775,104);&mul(425,243)%//{what()who()?{mul(842,148)how()<!who()@mul(197,181)@(~$ from()do()how()#-[&)who()$mul(254,640) what(){why(807,52)-+~!+who()mul(948,873)mul(127,689)~$*-mul(147,430)~!who()}where()where()mul(476,718)select(86,742)@!?when();from()do()>why()>why())+mul(96,44)mul(179,145):*~^what()~what()who(595,39)+mul(174,903)%?<]&~mul(13,307)how(98,997)}who()select()?^{:mul(858,7)]from()why()how()mul(681,532)from()when()from(){select()>[{(}mul(908,908) $,mul(221,664)!:)"

#matches = re.findall(regex2, test_str, re.MULTILINE)
matches = re.findall(regex2, inp_str, re.MULTILINE)

print (matches[0])
cleanMat = list(filter(None, matches))


#print (cleanMat[1])
#print (cleanMat[2])


print (len(matches))
print (len(cleanMat))
#print (cleanMat[-1])

updt_str = inp_str.replace(matches[0], '')

#print (updt_str)

addr = valMul(cleanMat[0])
print (addr)

subM = re.findall(regex1, updt_str, re.MULTILINE)


print (len(subM))

'''
i = 0 
for itms in subM:
    x = valMul(itms)

    i = i +1 
    addr = addr + x
'''


#print (addr)

last_str = r"]-who()-%-from()how()mul(338,481)how();why()@why()do()}from(){mul(196,713)@+(&^mul(35,164)mul(459,290)how(485,936)]]/"

y = valMul(last_str)

#print (y)

#print (addr+y)

# clean start

totMats = re.findall(regex1, inp_str, re.MULTILINE)

print (len(totMats))

midAddr = 0

for i,itms in enumerate(totMats):
    print ("next match, count is: ", i)
    midAddr = midAddr + valMul(itms)


print (midAddr)

print (matches[0])

firstAddr = valMul(matches[0])

print (firstAddr)

lastAddrStr = r"-who()-%-from()how()mul(338,481)how();why()@why()do()}from(){mul(196,713)@+(&^mul(35,164)mul(459,290)how(485,936)]]/"

lastAddr = valMul(lastAddrStr)

print (lastAddr)

print (midAddr + lastAddr + firstAddr)

chkStr = r"select()select()&(~!who()mul(450,794)where()}<how(638,85))select()[when()mul(987,169)!:who()who()]where()~mul(772,547){&{+'<)/mul(672!%>$<~do()-'when()$,who()where()(&[mul(216,443);mul(973,192)who(){)+?:$from()mul(711,798)mul(103,581)-*/',mul(634,298):~from()*'what()mul(908,815)who()@!what(),&[when()#from(566,230)"

#print (valMul(chkStr))

