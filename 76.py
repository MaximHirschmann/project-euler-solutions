# same as problem 31
limit = 100
table = {i:0 for i in range(-limit+1,limit+1)}
table[0] = 1
nums = [i for i in range(1, limit+1)]
for num in nums:
    for amount in range(1,limit+1):
        table[amount] += table[amount-num]
# -1 because only 100 is as a sum included
print(table[100]-1)