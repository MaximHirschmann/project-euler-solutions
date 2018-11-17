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


pandigital_multiplies = []
max_3 = 0
max_4 = 0
for i in reversed(range(5000,10000)):
    s = str(i)+str(2*i)
    if i <= max_4:
        break
    if isPandigital(s):
        pandigital_multiplies.append(int(s))
        max_4 = i

for i in reversed(range(192,342)):
    s = str(i)+str(2*i)+str(3*i)
    if i <= max_3:
        break
    if isPandigital(s):
        pandigital_multiplies.append(int(s))
        max_3 = i

print(max(pandigital_multiplies))
save_time(38,time()-start)