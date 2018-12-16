from math import log, ceil
from time import time

start = time()

lim = 6
nums = [[i] for i in range(2, lim+1)]
iterations = int(log(lim*2, 2))-1

def add_factor():
    global nums
    nums = [j+[i] for j in nums for i in range(j[-1], lim+1)]

def product(iterable):
    prod = 1
    for i in iterable:
        prod = prod * i
    return prod

solutions = {i:lim*10 for i in range(2,2*lim+1)}

for i in range(iterations):
    add_factor()
    new = []
    for j in nums:
        prod = product(j)
        if prod > lim*2:
            continue
        else:
            new.append(j)
            s = sum(j)
            ones = prod - s
            length = ones + i + 2
            if solutions[length] > prod:
                solutions[length] = prod
    nums = new

values = set()
for k, v in solutions.items():
    if k <= lim:
        values.add(v)
print(sum(values))
print(time()-start)