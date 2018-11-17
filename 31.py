from Utils import save_time
from time import time

start = time()

table = {i:0 for i in range(-199,201)}
table[0] = 1
coins = [1,2,5,10,20,50,100,200]
for coin in coins:
    for amount in range(1,201):
        table[amount] += table[amount-coin]

print(table[200])
save_time(31,time()-start)