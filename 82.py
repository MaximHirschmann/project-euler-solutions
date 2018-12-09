import copy

def smallest_neigbor(x, y, up = False):
    if up:
        if y != len(matrix)-1:
            return min([new[y][x], new[y+1][x] + matrix[y][x]])
        return new[y][x]
    else:
        if y == 0:
            return new[y][x-1]
        return min([new[y-1][x], new[y][x-1]])

with open("storage//81_matrix.txt",'r') as f:
    matrix = [list(map(int, line.replace("\n","").split(","))) for line in f]
new = copy.deepcopy(matrix)

for x in range(1, len(matrix[0])):
    # shortest path using down and left
    for y in range(len(matrix)):
        new[y][x] += smallest_neigbor(x, y)
    # if with top shorter then overwrite
    for y in reversed(range(len(matrix))):
        new[y][x] = smallest_neigbor(x, y, up = True)

print(min([i[-1] for i in new]))