from Utils import sieve_of_eratosthenes
from Utils import save_time
from time import time

start = time()

print("Sum: ",sum(sieve_of_eratosthenes(2000000)))

end = time()
save_time(10,end-start)