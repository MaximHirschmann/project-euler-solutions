from Utils import sum_of_proper_divisors

sums = {}

res = 0
for i in range(1,10000):
    sum = sum_of_proper_divisors(i)-i
    sums[i] = sum
    if sum in sums and sum != i and sums[sum] == i:
        res += i + sum
    
print("Res: ",res)