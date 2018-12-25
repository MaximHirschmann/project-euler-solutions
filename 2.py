def fib(k):
    if k in table:
        return table[k]
    else:
        value = fib(k-1)+fib(k-2)
        table[k] = value
        return value

#dynamic programming
table = {0:1, 1:1}
count, sum = 1, 0
while True:
    value = fib(count)
    if value >= 4000000:
        break
    if value%2 == 0:
        sum += value
    count += 1

print(sum)