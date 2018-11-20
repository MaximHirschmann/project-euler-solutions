from sympy import isprime
from Utils import bisect

res = 1
count = 2
number_primes = 0
number_numbers = 0
ratio = 1
while ratio >= 0.1:
    for _ in range(4):
        res += count
        if isprime(res):
            number_primes += 1
        number_numbers += 1
    ratio = number_primes/number_numbers
    count += 2
print((number_numbers-1)//2)

