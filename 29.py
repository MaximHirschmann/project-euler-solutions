from Utils import save_time
from time import time

start = time()

combinations = set()
for a in range(2,101):
    for b in range(2,101):
        combinations.add(a**b)
print(len(combinations))
save_time(29,time()-start)