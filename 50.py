from Utils import save_time
from time import time
from Utils import sieve_of_eratosthenes
from sympy import isprime

start_time = time()

sieve = sieve_of_eratosthenes(50000)
sums = {0:0}
for i in range(len(sieve)):
    sums[i+1] = sums[i] + sieve[i]

max = 0
for start in range(len(sieve)-50):
    for end in range(start+1, len(sieve)):
        add = sums[end] - sums[start]
        if add >= 1000000:
            break
        length = end-start
        if max < length:
            if isprime(add):
                max = length
                print(add,start,end, max)

save_time(50,time()-start_time)