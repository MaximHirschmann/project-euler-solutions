with open('storage//primes1000000.txt','r') as f:
    sieve = eval(f.read().replace('\n',''))
limit = 1000000
totients = [i for i in range(limit + 1)]

for i in sieve:
    factor = 1-(1/i)
    for j in range(1, int(((limit)/i)+1)):
        totients[i*j] *= factor

print(sum(map(round, totients))-1)