from itertools import combinations
from time import time

start = time()

def f(n):
    l = set(range(n))
    res = 0
    for length in range(2, n//2+1):
        for a in combinations(l, length):
            # all numbers in l that are not in a or smaller than min(a)
            others = list(l - set(a) - set(range(a[0]+1)))
            for b in combinations(others, length):
                # check if a or b always bigger than the other else res += 1
                s = sum([a[i] > b[i] for i in range(length)])
                if s != 0 and s != length:
                    res += 1
    return res

print(f(12))
print(time()-start)