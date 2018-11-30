# the less primefactors a number has the closer is the euler-totient to it
# can not be prime because p and p-1 do not have the same-digits
# checking every possible number with two factors yields the correct result
from sympy import factorint
from math import sqrt
from Utils import sieve_of_eratosthenes

# returns euler totient given the only two factors
def euler_totient(n, two_factors):
    return int(n * (1-(1/two_factors[0])) * (1-(1/two_factors[1])))

# True if a and b have the same digits
def samedigits(a,b):
    return sorted([int(i) for i in str(a)]) == sorted([int(i) for i in str(b)])

limit = 10**7
sieve = sieve_of_eratosthenes(int(sqrt(limit)*2))
min = 1000
for i, prime1 in enumerate(sieve):
    for j in range(i, len(sieve)):
        prime2 = sieve[j]
        product = prime1*prime2
        if product > limit:
            break
        eul = euler_totient(product, (prime1, prime2))
        if product/eul < min and samedigits(product, eul):
            min = (product)/eul
            min_prod = product

print(min_prod)