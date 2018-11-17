import itertools
from Utils import save_time
from time import time

start = time()

digits = ['0','1','2','3','4','5','6','7','8','9']

permutations = list(itertools.permutations(digits))

print(''.join(permutations[999999]))
save_time(24,time()-start)