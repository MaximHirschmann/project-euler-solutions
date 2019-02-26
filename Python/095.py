from sympy import divisors

limit = 1000000
sums = {1:0}

max_length = 0
min_value = limit

for i in range(1, limit//10):
    n = i
    chain = []
    while n:
        chain.append(n)
        if n > limit:
            chain.append(1)
            break
        if n in sums:
            n = sums[n]
        else:
            previous = n
            n = sum(divisors(n))-n
            sums[previous] = n
        if n in chain:
            if n != chain[0]:
                chain.append(1)
            break
    if chain[-1] != 1:
        if len(chain) > max_length:
            max_length = len(chain)
            min_value = i
print(min_value)