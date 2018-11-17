from Utils import save_time
from time import time
from itertools import product
from sympy import isprime as isPrime

start = time()

def remove_left_digit(n):
    return int(str(n)[1:])

def is_left_truncatable_prime(n):
    for i in range(len(str(n))-1):
        n = remove_left_digit(n)
        if not isPrime(n):
            return False
    return True

primes = ['2','3','5','7']
add = ['1','3','7','9']
products = [''.join(i) for i in product(primes,add)]
candidates = []

for i in range(7):
    for j in reversed(products):
        if not isPrime(j):
            products.remove(j)
    candidates += products
    products = [''.join(k) for k in product(products,add)]

print(sum(int(i) for i in candidates if is_left_truncatable_prime(int(i))))

save_time(37,time()-start)