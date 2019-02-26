from Utils import sieve_of_eratosthenes

# no need for euler totient function, because only small numbers
def recur_len(d):
    if d % 2 != 0 and d % 5 != 0 and d != 0 and d != 1:
        n = 1
        # every fraction 1/d can be written as x/(10**n - 1) where n is the length 
        # of the recurring cycle
        while (10**n - 1) % d != 0:
            n += 1
        return n

res = 0
res_index = 0
sieve = sieve_of_eratosthenes(1000,lower_limit=6)

for i in reversed(sieve):
    length = recur_len(i)
    if length > res:
        res = length
        res_index = i
    if i < res:
        break

print(res_index)