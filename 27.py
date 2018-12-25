from sympy import isprime
from Utils import sieve_of_eratosthenes

# where f(n) = n^2 + a*n + b
def number_of_primes(a,b):
    n = 0
    while isprime(n*n+a*n+b):
        n += 1
    return n

max_count = 0
sieve = sieve_of_eratosthenes(1000)
# a has to be odd
for a in range(-999,1000,2):
    # b has to be prime otherwise f(0) would not be prime
    # b can not be negative
    # a >= 1-b because n^2 + a*n + b >= 2 and if n = 1 then 1+a+n >= 2
    for b in reversed(sieve):
        if a < 1-b:
            break
        num = number_of_primes(a,b)
        if num > max_count:
            max_count = num
            prod = a*b

print(prod)