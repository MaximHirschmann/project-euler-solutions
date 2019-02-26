from itertools import permutations

def check(ring):
    last = ring[0] + ring[5] + ring[6]
    for i in range(3, len(indexes), 3):
        if ring[indexes[i]] + ring[indexes[i+1]] + ring[indexes[i+2]] != last:
            return False
    return True

indexes = [0, 5, 6, 1, 6, 7, 2, 7, 8, 3, 8, 9, 4, 9, 5]
res = 0
for i in permutations(range(7, 11)):
    for j in permutations(range(1, 6)):
        ring = [6] + list(i) + list(j)
        if check(ring):
            n = int(''.join([str(ring[i]) for i in indexes]))
            if n > res:
                res = n
print(res)