from Utils import sum_of_proper_divisors as sum_of_proper_divisors
from time import time
from Utils import save_time

start = time()
sums = {}

res = 0
for i in range(1,10000):
    sum = sum_of_proper_divisors(i)-i
    sums[i] = sum
    if sum in sums and sum != i and sums[sum] == i:
        res += i + sum
        print(sum, i)
print("Res: ",res)
save_time(21,time()-start)