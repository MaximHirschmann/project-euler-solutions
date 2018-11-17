from time import time
from Utils import save_time
from Utils import divisor_function

start = time()

def triangle_number(k):
    global table
    try:
        return table[k]
    except KeyError:
        number = triangle_number(k-1) + k
        table[k] = number
        return number

table = {0: 0}
k = 1
while True:
    n = triangle_number(k)
    if divisor_function(n) > 500:
        print(n)
        break
    k += 1

end = time()
save_time(12, end-start)