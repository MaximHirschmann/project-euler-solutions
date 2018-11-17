from time import time
from Utils import save_time

start = time()
def isPalindrom(n):
    s=str(n)
    if(s==s[::-1]):
      return True
    return False

max = 0
for i in reversed(range(100,1000)):
    if i * 999 <= max:
        break
    for j in reversed(range(i,1000)):
        product = i * j
        if product <= max:
            break
        if isPalindrom(product):
            max = product
print(max)
end = time()
save_time(4,end-start)