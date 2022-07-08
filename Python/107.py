from collections import deque
from time import time

from sortedcontainers import SortedList
from Utils import *

t0 = time()

class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        
    def other(self, v):
        if v == self.v1:
            return self.v2
        else:
            return self.v1
        
class Graph:
    def __init__(self, networkfile):
        matrix = []
        with open(networkfile, "r") as f:
            lines = f.read().split("\n")[:-1]
            for line in lines:
                matrix.append(line.split(","))

        self.adj = defaultdict(list)
        self.V = [i for i in range(len(matrix))]
        self.totalCost = 0
        self.edges = {}
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                weight = matrix[i][j]
                if weight == "-":
                    continue
                weight = int(weight)
                e = Edge(i, j, weight)
                self.adj[i].append(e)
                self.adj[j].append(e)
                self.totalCost += weight
                self.edges[(i, j)] = weight
                self.edges[(j, i)] = weight
        
G = Graph("storage//107_network.txt")

wert = []
pi = []
r = 0
for u in G.V:
    wert.append(float("inf"))
    pi.append(u)
wert[r] = 0

Q = G.V

while Q:
    u = Q.pop(0)
    for edge in G.adj[u]:
        v = edge.other(u)
        if v in Q and edge.weight < wert[v]:
            pi[v] = u
            wert[v] = edge.weight
    Q.sort(key = lambda x: wert[x])
    
total_weight = 0
for u, v in enumerate(pi):
    if u == v:
        continue
    total_weight += G.edges[(u, v)]
    
print("Complete Graph", G.totalCost)
print("Minimal spanning tree: ", total_weight)
print("Difference: ", G.totalCost - total_weight)

t1 = time()
save_time(107, t1-t0)
