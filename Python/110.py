import itertools
from sympy import factorint
from time import time

start = time()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
lowest = float("inf")
LIM = 4 * 10**6

for l in range(1, 7):
    for p in itertools.product((2,3,4,5,6), repeat = l):
        n = 1
        c = 1
        for i in range(len(primes)):
            if i < l:
                n *= primes[i] ** p[i]
                c *= (p[i] * 2 + 1)
            else:
                n *= primes[i]
                c *= 3
                
            if n > lowest:
                break
            
            if c > 2 * LIM - 1:
                lowest = min(lowest, n)
                break
            
print(lowest, factorint(lowest))
print(time() - start, "s")
