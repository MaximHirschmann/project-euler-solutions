from time import time
from Utils import save_time
from Utils import primefactors

start = time()

factors = primefactors(600851475143)
print("Largest prime factor:", max(k for k, v in factors.items()))

end = time()
save_time(3,end-start)

