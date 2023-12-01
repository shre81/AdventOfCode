import os
import numpy as np
import time
from collections import defaultdict
from heapq import *

#from exr15spa import dijsktra

#f = open("input-15-test", "r")
#f = open("input-15-test1", "r")
#f = open("input-15-test2", "r")
f = open("input-15", "r")

bigLst = f.read().splitlines()
#print (bigLst)
totRows = len(bigLst)
totCols = len(bigLst[0])
htArr = np.zeros((totRows, totCols), dtype=int)

# making a numpy array of what we get
for i, itms in enumerate(bigLst):
    for j, chrs in enumerate(itms):
        htArr[i][j] = int(chrs)

class Node():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __lt__(self, other):
        return self.X < other.X and self.Y < other.Y

initial = Node(htArr.shape[0]-1, htArr.shape[1]-1)
end = Node(0,0)
grphArr = htArr.copy()

#f = initial.copy()
#t = end.copy()
edges =grphArr.copy()


def dijkstra(edges, f, t):
    #g = defaultdict(list)
    #for l, r, c in edges:
    #    g[l].append((c, r))

    q, seen, mins = [(edges[f.X][f.Y], f, [])], set(), {f: edges[f.X][f.Y]}
    while q:
        (cost, v1, path) = heappop(q)
        # (0, f, [])
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1.X == t.X and v1.Y == t.Y:
                return (cost)
            #print (v1.X, v1.Y)
            NodeFath = Node(v1.X-1, v1.Y)
            NodeMoth = Node(v1.X, v1.Y-1)
            destinations = []
            if NodeFath.X>=0 and NodeFath.Y>=0:
                destinations.append(NodeFath)
            if NodeMoth.X>=0 and NodeMoth.Y>=0:
                destinations.append(NodeMoth)
            
            for v2 in destinations:
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + edges[v2.X][v2.Y]
                if prev is None or next < prev:
                    mins[v2] = next
                    #print ("type of next:" , type(next),"type of v2:" , type(v2), "type of path :" ,type(path))
                    heappush(q, (next, v2, path))

    return (float("inf"))


initial = Node(htArr.shape[0]-1, htArr.shape[1]-1)
end = Node(0,0)
grphArr = htArr.copy()

edges =grphArr.copy()

totCost = dijkstra(edges,initial,end)

print (totCost)

#for nods in lstOfNodes:
    #print (nods.X, nods.Y)
    #pass