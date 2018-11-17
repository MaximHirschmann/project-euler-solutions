from Utils import isPrime
from Utils import save_time
from time import time

start = time()

def prime_number(n):
    count = 0
    i = 0
    while True:
        if isPrime(i):
            count += 1
            if count == n:
                return i
        i += 1

print(prime_number(10001))
end = time()
save_time(7,end-start)