from Utils import save_time
from time import time

start = time()

print(sum([int(x) for x in str(2**1000)]))

end = time()
save_time(16,end-start)