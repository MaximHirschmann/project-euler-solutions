from itertools import permutations
from sympy import isprime
from Utils import save_time
from time import time

start = time()

digits = ('1','2','3','4','5','6','7','8','9')
perm = []
for i in range(1,len(digits)+1):
    perm += [int(''.join(i)) for i in permutations(digits[:i],i)]
perm = sorted(perm, reverse = True)

for i in perm:
    if isprime(i):
        print(i)
        break

save_time(41,time()-start)
