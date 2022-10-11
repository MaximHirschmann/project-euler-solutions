from collections import defaultdict
import itertools
from time import time
import functools

start = time()

def cubes(a, b, c, l):
    return 2 * (a * b + b * c + a * c) + 4 * (l-1) * (a + b + c + l - 2)

d = defaultdict(int)

search = 1000

LIM = 20000
max_dim = LIM
max_layer = 1000

for a in range(1, max_dim):
    for b in range(a, max_dim):
        if 2 * a * b > LIM:
            break
        for c in range(b, max_dim):
            if 2 * (a * b + b * c + a * c) > LIM:
                break
            for layer in range(1, max_layer):
                cubes_needed = cubes(a, b, c, layer)
                if cubes_needed > LIM:
                    break
                d[cubes_needed] += 1
    
for k,v in sorted(d.items()):
    if v == search:
        print(k)
        break

print(time() - start, "s")