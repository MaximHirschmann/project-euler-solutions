from sympy import isprime

res = 1
count = 2
primes = 0
total = 0
ratio = 1
while ratio >= 0.1:
    for _ in range(4):
        res += count
        if isprime(res):
            primes += 1
        total += 1
    ratio = primes/total
    count += 2
print((total-1)//2)