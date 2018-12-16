def product(iterable):
    prod = 1
    for i in iterable:
        prod *= i
    return prod

def factors(number, max_factor=10000000):
    if number in mem_factors:
        return mem_factors[number]
    result = []
    factor = min(number // 2, max_factor)

    while factor >= 2:
        if number % factor == 0:
            divisor = number // factor
            if divisor <= factor and divisor <= max_factor:
                result.append([factor, divisor])
            result.extend([factor] + item for item in factors(divisor, factor))
        factor -= 1

    mem_factors[number] = result
    return result

lim = 12000
mem_factors = {}
solutions = {k: 2*k for k in range(2, lim+1)}

for i in range(2, 2*lim+1):
    for j in factors(i):
        p = product(j)
        length = p - sum(j) + len(j)
        if length <= lim and p < solutions[length]:
            solutions[length] = p

print(sum(set(solutions.values())))