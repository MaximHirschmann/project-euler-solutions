def digitsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

maximum = 0
for a in range(100):
    for b in range(100):
        ds = digitsum(a**b)
        if ds > maximum:
            maximum = ds
print(maximum)

