from cProfile import run
import os
import string

f = open("input-7-test", "r")
#f = open("input-7", "r")

allLst = f.read().splitlines()

def cmdOrOp(some_string):
    if (some_string[0] == '$'):
        if (some_string[2:4] == 'cd'):
            chkDir = 1
        elif (some_string[2:4] == 'ls'):
            chkDir = 2
            

print (allLst)
