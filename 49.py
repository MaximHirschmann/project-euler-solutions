from Utils import sieve_of_eratosthenes

def samedigits(a,b):
    a = sorted(str(a))
    b = sorted(str(b))
    return a == b

sieve = sieve_of_eratosthenes(9999,lower_limit=1000)
for i in range(len(sieve)-1):
    prime1 = sieve[i]
    for j in range(i+1,len(sieve)):
        prime2 = sieve[j]
        # test if same digits
        if samedigits(prime1,prime2):
            prime3 = 2*prime2 - prime1
            # test if prime3 is prime
            if prime3 in sieve and samedigits(prime1,prime3):
                concat = str(prime1)+str(prime2)+str(prime3)
                if concat != '148748178147':
                    print(concat)