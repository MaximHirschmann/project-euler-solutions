from math import gcd

limit = 1000000
closest = 2/5
target = 3/7
for d in range(2, limit):
    if d % 7 == 0:
        continue
    for n in range(int((target - closest*target)*d), int(target*d)+1):
        distance = abs(n/d - target)
        if closest > distance:
            closest = distance
            numerator = n
print(numerator)