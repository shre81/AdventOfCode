import os
#from typing_extensions import final
import numpy as np
import re
import string
from itertools import cycle, repeat

#f = open("input-10-test", "r")
f = open("input-10", "r")

bigLst = f.read().splitlines()

lstOfBrkt = [('[', ']'), ('<', '>'), ('{', '}'), ('(', ')')]
chkStrLst = ['[]', '{}', '<>', '()']
regLst = [r"\<>", r"\[]", r"\{}", r"\(\)"]
regex = r"\<>"
subst = ""


def elimPatt(someStr):
    #print (type(someStr))
    if any(strPats in someStr for strPats in chkStrLst):
        pass
    else:
        return someStr
    
    for itms in cycle(regLst):
        if any(strPats in someStr for strPats in chkStrLst):
            subst = ""
            newStr = re.sub(itms, subst, someStr, 0, re.MULTILINE)
            someStr = newStr
            if (len(newStr)==len(someStr)):
                continue
            else:
                elimPatt(someStr) 
        else:
            break

    return someStr

chkStrLst = ['[]', '{}', '<>', '()']
regLst = [r"\<>", r"\[]", r"\{}", r"\(\)"]

openers = ['[', '{', '<', '(']
closers = [']', '}', '>', ')']

wrongOnes = {}
incompOnes = {}
for idx, vals in enumerate(bigLst):
    retStr = elimPatt(vals)
    #print ("for the line number: ", idx, " the pruned value is: ", retStr)
    if (any(itms in closers for itms in retStr)):
        #print ("inside this loop for: ", retStr, "and the original string was: ", vals)
        res = next((ele for ele in retStr if ele in closers), None)
        wrongOnes[idx] = res
    else:
        incompOnes[idx] = retStr

#print (incompOnes)

def calcMiddle(incDct):
    valDct = {'(': 1, '[': 2, '{':3, '<':4 }
    tmpDct = {}
    for k,v in incDct.items():
        revV = reversed(v)
        summer = 0
        oldsum = 0 
        for chrs in revV:
            newSum = oldsum*5 + valDct[chrs]
            oldsum = newSum
        tmpDct[k] = oldsum

    lstOfInt = sorted(tmpDct.values())
    midLe = int(len(lstOfInt)/2)

    return lstOfInt[midLe]

print (calcMiddle(incompOnes))

# Part 1 below
""" def totErr(dctOfErrs):
    errDct = {')':3, ']':57, '}':1197, '>':25137}
    summer = 0
    for k,v in dctOfErrs.items():
        summer += errDct[v]
    return summer

print (totErr(wrongOnes)) """

