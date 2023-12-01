import os
import numpy as np
import string as str

#f = open("input-12-test", "r")
f = open("input-12-test1", "r")
#f = open("input-12", "r")

bigLst = f.read().splitlines()

#print (bigLst)


makTupLst = []
for itms in bigLst:
    makTupLst.append(tuple(itms.split('-')))
print (makTupLst)

strtLst = []
endLst = []
nonTerms = []

for itms in makTupLst:
    if 'start' in itms:
        if 'start' in itms[1]:
            newTup = (itms[1], itms[0])
        else:
            newTup = itms
        strtLst.append(newTup)
    elif 'end' in itms:
        if 'end' in itms[0]:
            newTup = (itms[1], itms[0])
        else:
            newTup = itms
        endLst.append(newTup)
    else:
        nonTerms.append(itms)

smlSeen = []

print ("only starters in: " , strtLst)
print ("only enders in : ",  endLst)
print ("all the rest in: ", nonTerms)

flpdLst = nonTerms.copy()

for oths in nonTerms:
    if oths[1].isupper() or oths[0].isupper():
        print (oths, " is all caps")
        flipPath = (oths[1], oths[0])
        flpdLst.append(flipPath)

print ("after flipping: ", flpdLst)

bigFatLst = strtLst + flpdLst + endLst

print (bigFatLst)

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)



def findPaths(someLst):
    seenPoints = []

    for idx, pts in enumerate(someLst):
        if (pts[0]=='start'):
            thisPath.append(pts)
            seen.append(pts)
            newStart = pts[1]
    
    for idx, pts in enumerate(someLst):
        if (pts[0]==newStart) & (pts not in seen):
            thisPath.append(pts)
            seen.append(pts)

    




for st in strtLst:
    for oths in makTupLst:
        for i in (0,1):
            if oths[i] in st:
                #print (oths, " is a connector")
                pass