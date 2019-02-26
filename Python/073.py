from math import ceil

def frac(d):
    sieve = [0] * (d + 1)
    for denominator in range(5, d + 1):
        if denominator % 3 == 0:
            lower_limit = denominator // 3 + 1
        else:
            lower_limit = ceil(denominator / 3)
        if denominator % 2 == 0:
            upper_limit = denominator // 2 - 1
        else:
            upper_limit = denominator // 2
        # add range of numbers which are > 1/3 and < 1/2
        sieve[denominator] += upper_limit - lower_limit + 1
        # substract multiples of already found fractions
        for j in range(2 * denominator, d + 1, denominator):
            sieve[j] -= sieve[denominator]
    return sum(sieve)

print(frac(12000))