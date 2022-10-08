from Utils import sieve_of_eratosthenes
from time import time
from sympy import factorint
import datetime
from math import log, ceil
from itertools import accumulate

LIM = 1000
expected = 9


print(datetime.datetime.now())
start = time()

def c(n):
    result = 1
    for prime, exp in factorint(n).items():
        if prime == 3:
            if exp != 1:
                result *= 3
        
        if prime % 3 == 1:
            result *= 3
    
    return result

def helper(expected):
    if expected == 9:
        return 7
    elif expected == 27:
        return 7 * 9
    elif expected == 81:
        return 7 * 9 * 13
    elif expected == 243:
        return 7 * 9 * 13 * 19
    elif expected == 729:
        return 7 * 9 * 13 * 19 * 31
    else:
        print("Expected too big or not a power of 3")
        return 1

maximum = (LIM // helper(expected)) + 1
primes = sieve_of_eratosthenes(maximum)
elite_primes = sorted([(prime ** exponent, prime) for prime in primes for exponent in range(1, ceil(log(maximum) / log(prime))) if (prime % 3 == 1 or (prime == 3 and exponent != 1))])

t_sieve = time()
print("Sieve calculated in", t_sieve-start, "s")

rec_2_helper = list(accumulate(n if c(n) == 1 else 0 for n in range((LIM // helper(expected * 3))+1)))
rec_2_helper2 = list(accumulate(n if c(n) == 1 and n % 3 != 0 else 0 for n in range((LIM // helper(expected * 3))+1)))
    
print("MEM calculated in", time()-t_sieve, "s")

def multiplier(n, left):
    if left == 1:
        return 1
    elif left == 2:
        return 3
    
    if n % 3 == 0:
        return rec_2_helper2[left]
    else:
        return rec_2_helper[left]
    
def rec(current, i, score):
    if score == expected:
        return current * multiplier(current, LIM // current)
    
    s = 0
    while i < len(elite_primes):
        factor, prime = elite_primes[i]
        if current % prime != 0:
            product = current * factor
            if product > LIM:
                break
            s += rec(product, i + 1, score * 3)
        i += 1
    return s
  
t1 = time()
print("SUM:", rec(1, 0, 1))
t2 = time()
print(t2 - t1, "s for Recursion")

print(time() - start, "s")