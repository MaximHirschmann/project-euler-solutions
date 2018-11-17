from Utils import save_time
from time import time
from Utils import sieve_of_eratosthenes
from math import sqrt

start = time()

limit = 10000

sieve = sieve_of_eratosthenes(limit)
twice_squares = [2*(i**2) for i in range(int(sqrt(limit)))]

for i in range(3,int(0.9*limit),2):
    possible = False
    j = 0
    while sieve[j] <= i:
        if i-sieve[j] in twice_squares:
            possible = True
            break
        j += 1
    if not possible:
        print(i)
        break

save_time(46,time()-start)