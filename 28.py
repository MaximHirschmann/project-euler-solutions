from Utils import save_time
from time import time

start = time()
# returns n-th number of the spiral
def f(n):
    if n in table:
        return table[n]
    res = f(n-1)+2*(int((n-1)/4))+2
    table[n] = res
    return res

table = {0:1}

d = 1001
print(sum(f(i) for i in range(2*d-1)))
save_time(28,time()-start)