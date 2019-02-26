from Utils import sum_of_proper_divisors
from time import time

sums = {0:0}

res = 0
for i in range(1, 10000):
    sum = sum_of_proper_divisors(i)-i
    sums[i] = sum
    if sum < i and sums[sum] == i:
        res += i + sum
    
print(res)