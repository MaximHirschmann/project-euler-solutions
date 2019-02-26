from math import factorial

def sum_factorial_digits(n):
    return sum([fac[int(i)] for i in str(n)])

fac = {i:factorial(i) for i in range(10)}
print(sum([i for i in range(3,2540160) if i == sum_factorial_digits(i)]))