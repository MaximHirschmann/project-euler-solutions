from math import factorial as factorial
from Utils import save_time
from time import time

start = time()

print(sum(int(i) for i in str(factorial(100))))

save_time(20,time()-start)