from math import log
from Utils import sieve_of_eratosthenes

limit = 20
sieve = sieve_of_eratosthenes(limit)
res = 1
for i in sieve:
    l = log(limit, i)
    res *= i**(int(l))
print(res)