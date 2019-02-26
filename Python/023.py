from Utils import sum_of_proper_divisors
import time

start = time.time()
abundant = [i for i in range(2,28123) if sum_of_proper_divisors(i)-i>i]

sums = {i:False for i in range(28123)}

for i in abundant:
    print(i)

for i in range(len(abundant)):
    for j in range(i,len(abundant)):
        sum_abundant = abundant[i]+abundant[j]
        sums[sum_abundant] = True
        if sum_abundant > 28123:
            break

print(sum([k for k,v in sums.items() if not v]))
print(time.time()-start)