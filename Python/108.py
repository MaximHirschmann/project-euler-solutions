from sympy import factorint
from time import time

start = time()

def count(n):
    f = factorint(n)
    p = 1
    for _, v in f.items():
        p *= (2*v + 1)
    
    return (p + 1) // 2
    
LIM = 10000
high = 0

n = 1
while True:
    c = count(n)
    if c > high:
        high = c
        print(n, high, factorint(n))
        
    if c > LIM:
        print(n, factorint(n))
        break
    n += 1
    
print(time() - start, "s")