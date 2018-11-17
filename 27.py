from Utils import isPrime
from Utils import sieve_of_eratosthenes
from Utils import save_time
from time import time

start = time()

# where f(n) = n^2 + a*n + b
def number_of_primes(a,b):
    n = 0
    while(isPrime(n*n+a*n+b)):
        n += 1
    return n

max_count, max_a, max_b = 0,0,0
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
            max_a = a
            max_b = b
print('The function f(n) = n^2 +',max_a,'* n +', max_b,' produces with',max_count,'the most primes')
print('Product:',max_a * max_b)
save_time(27,time()-start)
      

