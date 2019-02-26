from Utils import sieve_of_eratosthenes
from sympy import isprime

sieve = sieve_of_eratosthenes(50000)
sums = {0:0}
for i in range(len(sieve)):
    sums[i+1] = sums[i] + sieve[i]

max = 0
max_number = 0
for start in range(len(sieve)-50):
    for end in range(start+1, len(sieve)):
        add = sums[end] - sums[start]
        if add >= 1000000:
            break
        length = end-start
        if max < length and isprime(add):
            max = length
            max_number = add
print(max_number)