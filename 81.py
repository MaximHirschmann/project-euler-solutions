def smallest_neighbor(i, j):
    neighbors = []
    if i != 0:
        neighbors.append(matrix[i-1][j])
    if j != 0:
        neighbors.append(matrix[i][j-1])
    return min(neighbors, default = 0)

with open("storage//81_matrix.txt",'r') as f:
    matrix = [list(map(int, line.replace("\n","").split(","))) for line in f]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] += smallest_neighbor(i, j)

print(matrix[-1][-1])