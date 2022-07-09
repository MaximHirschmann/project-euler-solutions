import numpy as np
from functools import lru_cache

from time import time

start = time()

# matrix of the graph
P = np.array([
    [0, 1/2, 0, 0, 0, 1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1/3, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1/3, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1/3, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1/2, 0, 0, 0, 0, 0, 1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1/3, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/4, 0, 0, 0, 1/4, 0, 1/4, 0, 0, 0, 1/4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 1/3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/2, 0, 0, 0, 0, 0, 1/2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 1/3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 1/3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1/3, 0, 1/3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/2, 0, 0, 0, 1/2, 0],
])


ITERATIONS = 3000
DIM = 5

dist_cache = {}

def coord_to_idx(coord):
    return coord[0] * DIM + coord[1]

def in_cache_dist(pos, seeds):
    coords_pos = (pos // DIM, pos % DIM)
    
    pos2 = coord_to_idx((DIM - coords_pos[0] - 1, DIM - coords_pos[1] - 1))
    pos3 = coord_to_idx((DIM - coords_pos[0] - 1, coords_pos[1]))
    pos4 = coord_to_idx((coords_pos[0], DIM - coords_pos[1] - 1))
    
    coords_seeds = tuple(sorted((seed // DIM, seed % DIM) for seed in seeds))
    seeds2 = tuple(sorted(coord_to_idx((DIM - y - 1, DIM - x - 1)) for y, x in coords_seeds))
    seeds3 = tuple(sorted(coord_to_idx((DIM - y - 1, x)) for y, x in coords_seeds))
    seeds4 = tuple(sorted(coord_to_idx((y, DIM - x - 1)) for y, x in coords_seeds))
    
    if (pos, seeds) in dist_cache:
        return dist_cache[(pos, seeds)]
    if (pos2, seeds2) in dist_cache:
        return list(reversed(dist_cache[(pos2, seeds2)]))
    if (pos3, seeds3) in dist_cache:
        return dist_cache[(pos3, seeds3)]
    if (pos4, seeds4) in dist_cache:
        return list(reversed(dist_cache[(pos4, seeds4)]))
    return False

def distribution(pos, seeds):
    cache = in_cache_dist(pos, seeds)
    if cache:
        return cache
    
    avg_steps = np.zeros(len(seeds))
    probabilities = np.zeros(len(seeds))
    
    # markov chain
    # simulate distribution over time (steps)
    v = np.zeros(DIM * DIM)
    v[pos] = 1
    
    for i in range(1, ITERATIONS):
        v = v @ P
        
        for j, seed in enumerate(seeds):
            probabilities[j] += v[seed]
            avg_steps[j] += i * v[seed]
            # a seed was reached, do not look at paths from here on
            # we are only looking for the first seed reached
            # this makes it so that the sum(v) approaches 0
            v[seed] = 0
            
    
    for i in range(len(seeds)):
        avg_steps[i] /= probabilities[i]
        
    res = [(probabilities[i], avg_steps[i]) for i in range(len(seeds))]
    dist_cache[(pos, seeds)] = res
    return res

# returns avg steps from pos with seeds at positions in bottom and empty fields in top
@lru_cache(maxsize=None)
def calculate(pos, bottom, top):
    if len(bottom) == 0:
        return 0
    
    # how relatively likely it is to reach each field with a seed from pos
    down = distribution(pos, bottom)
    # how relatively likely it is to reach each field from the bottom starting at a field with a seed
    ups = [distribution(i, top) for i in bottom]

    # 
    steps = 0
    for i in range(len(down)):
        p, s = down[i] # probability, avg_steps
        for j in range(len(ups[i])):
            p2, s2 = ups[i][j]
            new_pos = top[j]
            new_bottom = tuple(k for k in bottom if k != bottom[i])
            new_top = tuple(k for k in top if k != top[j])
            # recursive
            s3 = calculate(new_pos, new_bottom, new_top)
            
            steps += (s + s2 + s3) * p * p2
    
    return steps

res = calculate(12, (20, 21, 22, 23, 24), (0, 1, 2, 3, 4))
print(res)

end = time()

print()
print(end-start, "s")