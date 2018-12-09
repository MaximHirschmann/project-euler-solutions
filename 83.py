# modified version of https://blog.dreamshire.com/project-euler-83-solution/
import networkx as nx

with open("storage//81_matrix.txt",'r') as f:
    matrix = [list(map(int, line.replace("\n","").split(","))) for line in f]
n, m = len(matrix), len(matrix[0])

G = nx.DiGraph()
for i in range(n):
    for j in range(m):
        neighbors = []
        adjacent = ((-1,0), (0,-1), (1,0), (0,1))
        for a, b in adjacent:
            if 0 <= i+a < n and 0 <= j+b < m:
                neighbors.append((i+a,j+b))
        for c, d in neighbors:
            G.add_edge((i, j), (c,d), weight = matrix[c][d])

print(nx.dijkstra_path_length(G, source=(0,0), target=(n-1,m-1)) + matrix[0][0])