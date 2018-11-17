# a number is divisible by the divisor without a remainder 
# if the primefactors of the dividend contains all primefactors of
# the divisor at least as many times as the divisor

from Utils import primefactors
from Utils import save_time
from collections import Counter
from time import time

start = time()

primes = [2,3,5,7,11,13,17,19]
primes_max_occurence = {2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}

# finds the primefactors of the searched number
for i in range(2,20):
    factors = primefactors(i)
    counted = Counter(factors)
    for j in factors:
        if primes_max_occurence[j] < counted[j]:
            primes_max_occurence[j] = counted[j]

# multiplies the primefactors
product = 1
for i in primes:
    product = product * (i**primes_max_occurence[i])
print("Product: ",product)
end = time()
save_time(5,end-start)