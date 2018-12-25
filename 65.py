from math import gcd
from Utils import digitsum

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

    return  (last[1], last[0])


limit = 100
# there is a pattern in the continued fraction
# 2,1,2,1,1,4,1,1,6,1,1,8 ...
sequence = [2, 1]
for i in range(2, limit):
    if i % 3 == 2:
        sequence.append((i//3) * 2 + 2)
    else:
        sequence.append(1)
print(digitsum(to_fraction(sequence)[0]))