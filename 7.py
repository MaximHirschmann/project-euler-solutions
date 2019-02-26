from sympy import isprime

# returns n'th prime
def prime_numbers(n):
    count = 0
    i = 2
    while True:
        if isprime(i):
            count += 1
            if count == n:
                return i
        i += 1

print(prime_numbers(10001))