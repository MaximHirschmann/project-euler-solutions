from time import time
from Utils import save_time
import sys

start = time()

with open(sys.path[0]+"/storage/13.txt","r") as f:
    print(str(sum(map(int,f.read().split("\n"))))[:10])

end = time()
save_time(13,end-start)