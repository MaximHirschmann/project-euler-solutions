from Utils import save_time
from time import time

start = time()

print(str(sum([i ** i for i in range(1, 1001)]))[-10:])

save_time(48,time()-start)