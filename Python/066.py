from math import sqrt, gcd

def is_square(n):
    root = sqrt(n)
    return int(root) == root

# returns sequence of first 100 numbers
def continued_fraction(n):
    m = 0
    d = 1
    a0 = int(sqrt(n))
    a = a0
    sequence = [a]
    for _ in range(1000):
        m = d * a - m
        d = (n - m*m)/d
        a = int((a0 + m)/d)
        sequence.append(a)
    return sequence

# returns fraction from a sequence
def to_fraction(sequence):
    last = [1, sequence[-1]]
    sequence.pop(-1)
    count = 0
    for i in reversed(sequence):
        last[0] = i * last[1] + last[0]
        last[0], last[1] = last[1], last[0]
        count += 1
    divisor = 0
    while divisor != 1:
        divisor = gcd(last[0], last[1])
        last = [last[0]//divisor, last[1]//divisor]
    return  [last[1], last[0]]

max_x = 0
max_index = 0
for D in range(2,1000):
    if not is_square(D):
        con = continued_fraction(D)
        for j in range(1, len(con)):
            frac = to_fraction(con[:j])
            # frac[0] = x, frac[1] = y
            if frac[0]*frac[0] - D * frac[1]*frac[1] == 1:
                if frac[0] > max_x:
                    max_x = frac[0]
                    max_index = D
                break
print(max_index)