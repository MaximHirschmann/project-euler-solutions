# https://projecteuler.net/overview=069
from sympy import isprime

count = 0
i = 2
product = 1
while count < 7:
    if isprime(i):
        product *= i
        count += 1
    i += 1
print(product)