import itertools
from sympy import isprime
from time import time

start = time()

n = 10
res = 0

for d in range(10):
    S = 0
            
    for length in range(1, n):
        for places in itertools.combinations(range(n), length):
            for replacements in itertools.product(range(10), repeat = length):
                if d in replacements:
                    continue
                
                connected = ""
                j = 0
                for i in range(n):
                    if i in places:
                        connected += str(replacements[j])
                        j += 1
                    else:
                        connected += str(d)
                number = int(connected)
                
                if len(str(number)) != n:
                    continue
                
                if isprime(number):
                    S += number
        if S != 0:
            break

    res += S
    
print(res)
    
print(time() - start, "s")