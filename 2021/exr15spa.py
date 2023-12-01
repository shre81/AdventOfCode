import os
import numpy as np
import time
from collections import defaultdict
import heapq as heap

#f = open("input-15-test", "r")
f = open("input-15-test1", "r")
#f = open("input-15-test2", "r")
#f = open("input-15", "r")

bigLst = f.read().splitlines()
#print (bigLst)
totRows = len(bigLst)
totCols = len(bigLst[0])
htArr = np.zeros((totRows, totCols), dtype=int)

# making a numpy array of what we get
for i, itms in enumerate(bigLst):
    for j, chrs in enumerate(itms):
        htArr[i][j] = int(chrs)
        
initial = (2,2)
end = (0,0)

class Node():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, graph[initial.X][initial.Y])}
    nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode)
    current_node = initial
    visited = set()
    
    #print (current_node.X, current_node.Y)

    while (current_node.X, current_node.Y) != (end.X, end.Y):
        #print (" yes, current_node = ", current_node.X, current_node.Y, " is not equal to ", end.X, end.Y)
        visited.add(current_node)
        NodeFath = Node(current_node.X-1, current_node.Y)
        NodeMoth = Node(current_node.X, current_node.Y-1)
        destinations = []
        if NodeFath.X>=0 and NodeFath.Y>=0:
            destinations.append(NodeFath)
        if NodeMoth.X>=0 and NodeMoth.Y>=0:
            destinations.append(NodeMoth)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[next_node.X][next_node.Y] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    totWt = 0
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        #totWt = shortest_paths[current_node][1]
        current_node = next_node

    for pths in path:
        totWt += graph[pths.X][pths.Y]
    totWt = totWt - graph[end.X][end.Y]
    # Reverse path
    #path = path[::-1]
    return totWt

print (htArr.shape)
initial = Node(htArr.shape[0]-1, htArr.shape[1]-1)
end = Node(0,0)
grphArr = htArr.copy()

currWt = dijsktra(grphArr, initial, end)

print (currWt)
