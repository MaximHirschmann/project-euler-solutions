from Utils import save_time
from time import time

start = time()
with open('storage//22_names.txt','r') as f:
    names=list(eval(f.read()))
    names.sort()

def name_score(name, index):
    return sum(ord(i)-64 for i in name) * (index+1)

print(sum(name_score(names[i],i) for i in range(len(names))))
save_time(22,time()-start)