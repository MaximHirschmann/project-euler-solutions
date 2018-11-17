from Utils import save_time
from time import time

start = time()

def sum_of_power_digits(n, power):
    digits = []
    while n != 0:
        mod = n % 10
        digits.append(mod)
        n = int((n-mod)/10)
    digits = tuple(sorted(digits))
    if digits in table:
        return table[digits]
    res = sum([i**power for i in digits])
    table[digits] = res
    return res

table = {}
sum_nums = 0
for i in range(10,354294):
    if (i==sum_of_power_digits(i,5)):
        sum_nums += i
print(sum_nums)

save_time(30,time()-start)