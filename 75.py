from math import gcd
from collections import Counter

# euclids algorithm
def find_single_triples(limit):
    solutions = []
    lim = int((limit // 2 - 1)**0.5) + 1
    for m in range(2, lim):
        for n in range(1, m):
            perimeter = 2*m * (m + n)
            if perimeter > limit:
                break
            if (m % 2 == 0 or n % 2 == 0) and gcd(m, n) == 1:
                k_max = limit // perimeter
                for k in range(1, k_max + 1):
                    solutions.append(k * perimeter)
    return sum(1 for v in Counter(solutions).values() if v == 1)

print(find_single_triples(1500000))