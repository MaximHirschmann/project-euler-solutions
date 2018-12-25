# same as 76 only nums is different
from Utils import sieve_of_eratosthenes
limit = 1000
table = {i:0 for i in range(-limit+1,limit+1)}
table[0] = 1
nums = sieve_of_eratosthenes(limit)
for num in nums:
    for amount in range(1,limit+1):
        table[amount] += table[amount-num]
for k, v in table.items():
    if v > 5000:
        print(k)
        break