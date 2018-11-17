from Utils import save_time
from time import time

start = time()

def isPandigital(s):
    numbers={i:False for i in range(1,10)}
    for j in s:
        numbers[int(j)]=True
    for i in range(1,10):
        if not numbers[i]:
            return False
    return True

products = set()
for small in range(1,100):
    for big in range(small,10000):
        product = small * big
        if len(str(product)) == 4:
            if isPandigital(str(small)+str(big)+str(product)):
                products.add(product)

print(sum(products))
save_time(32,time()-start)
