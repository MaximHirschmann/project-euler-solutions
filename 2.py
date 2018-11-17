from time import time
from Utils import save_time

start = time()
def fib(k):
    global table
    try:
        return table[k]
    except KeyError:
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

print("The sum is: ",sum)
end = time()
save_time(2,end-start)