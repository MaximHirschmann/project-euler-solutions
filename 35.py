from Utils import sieve_of_eratosthenes

def rotate(s):
    return s[len(s)-1]+s[:len(s)-1]

sieve = sieve_of_eratosthenes(999999)
table = {k:False for k in range(1000000)}
for i in sieve:
    table[i] = True

circular_primes = []
count = 0
for i in sieve:
    if i not in circular_primes:
        s = str(i)
        rotations = []
        for k in s:
            s = rotate(s)
            rotations.append(int(s))
            if not table[int(s)]:
                rotations = []
                break
        circular_primes += rotations
            

print(len(set(circular_primes)))