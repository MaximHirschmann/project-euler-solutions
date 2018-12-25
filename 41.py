from itertools import permutations
from sympy import isprime

digits = ('1','2','3','4','5','6','7','8','9')
perms = sorted([int(''.join(j)) for i in range(1, len(digits)+1) for j in permutations(digits[:i], i)], reverse = True)

for i in perms:
    if isprime(i):
        print(i)
        break