import re

regex = r"(.*)(?=don't[(][)])"
regex2= r"(.*)(?=don't[(][)])"
test_str = "]@;why()]&where()@select()mul(589,854)${ <-}$how()^#mul(517,928)^(%@#who()@'mul(82,659):don't()mul(670,226)when(626,911)from()&%{%where())-mul(244,869)<]mul(582,125)<mul(219,47):'!mul(95,365)select(){how()how()select()mul(273,775)[$!],?)@mul(955,698)what()where()/;mul(79,369)&?*$do()from()@mul(994,313)what()mul(603,3)'~@]'@@mul(729,217)#-/mul(561,454)!mul(588,577)^%'{mul(705,583){*;+;mul(418,129)~@:^mul(449,366)@what()},-)):^*mul(842,848)%what()where():what()))<from()/mul(775,104);&mul(425,243)%//{what()who()?{mul(842,148)how()<!who()@mul(197,181)@(~$ from()do()how()#-[&)who()$mul(254,640) what(){why(807,52)-+~!+who()mul(948,873)mul(127,689)~$*-mul(147,430)~!who()}where()where()mul(476,718)select(86,742)@!?when();from()do()>why()>why())+mul(96,44)mul(179,145):*~^what()~what()who(595,39)+mul(174,903)%?<]&~mul(13,307)how(98,997)}who()select()?^{:mul(858,7)]from()why()how()mul(681,532)from()when()from(){select()>[{(}mul(908,908) $,mul(221,664)!:)"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))