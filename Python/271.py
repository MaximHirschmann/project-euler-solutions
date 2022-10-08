from sympy import factorint
from functools import reduce
import itertools
from time import time

start = time()

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod 

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
n = 13082761331670030
factors = factorint(n)

if not all(i == 1 for i in list(factors.values())):
    raise ValueError("Only supported for numbers where the prime factorization has each prime only once")

factors = list(factors.keys())

mem = {}
for prime in factors:
    found = [1]
    for x in range(2, prime):
        if x**3 % prime == 1:
            found.append(x)
    mem[prime] = found
    
    
solutions = []
for remainders in itertools.product(*mem.values()):
    if all(i == 1 for i in remainders): # only ones yield 1 ≡ 1 (mod n)
        continue
    
    solutions.append(chinese_remainder(factors, list(remainders)))
    
print(sum(solutions))

print(time() - start, "s")