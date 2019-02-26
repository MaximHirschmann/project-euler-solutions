from math import sqrt

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def length_continued_fraction(n):
    m = 0
    d = 1
    a0 = int(sqrt(n))
    a = a0
    count = 0
    found_triples = []
    while True:
        m = d * a - m
        d = (n - m*m)/d
        a = int((a0 + m)/d)
        if (m, d, a) in found_triples:
            break
        found_triples.append((m, d, a))
        count += 1
    return count

squares = [x*x for x in range(100)]
count = 0
for i in range(2,10000):
    if i not in squares:
        if length_continued_fraction(i) % 2 == 1:
            count += 1
print(count)