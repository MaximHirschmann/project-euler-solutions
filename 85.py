from time import time
from Utils import save_time

start = time()
def num(m, n):
    return int(((m * (m+1))/2) * ((n * (n+1))/2))

limit = 2000000
current = 0

for m in range(1, limit):
    for n in range(1, m):
        res = num(m, n)
        if res > limit:
            break
        if res > current:
            current = res
            area = m*n
        
print(area)
save_time(85, time()-start)