from sympy import isprime

# counts prime numbers up to n
def prime_numbers(n):
    count = 0
    i = 0
    while True:
        if isprime(i):
            count += 1
            if count == n:
                return i
        i += 1

print(prime_numbers(10001))