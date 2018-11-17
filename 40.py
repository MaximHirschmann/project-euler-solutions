from Utils import save_time
from time import time

start = time()

s = ""
length = 0
number = 0
while length <= 1000000:
    s_number = str(number)
    s += s_number
    length += len(s_number)
    number += 1

product = 1
for i in range(6):
    product *= int(s[10**i])
print(product)

save_time(40,time()-start)