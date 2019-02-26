from Utils import sieve_of_eratosthenes

limit = 50000000
sieve = sieve_of_eratosthenes(int(limit**(1/2))+1)
memory = {}

for a in sieve:
    for b in sieve:
        ab = a**2 + b**3
        if ab >= limit:
            break
        for c in sieve:
            res = c**4 + ab
            if res < limit:
                memory[res] = 1
            else:
                break

print(sum(memory.values()))