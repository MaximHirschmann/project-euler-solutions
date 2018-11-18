from Utils import sieve_of_eratosthenes
from sympy import isprime

def number_primes(number ,binary):
    count = 0
    last_prime = 0
    number = str(number)
    for digit in ('9','8','7','6','5','4','3','2','1','0'):
        new = ''
        for b in range(len(binary)):
            if binary[b] == '1':
                new += str(digit)
            else:
                new += number[b]
        new += number[-1]
        if isprime(int(new)) and new[0] != '0':
            last_prime = new
            count += 1
    return (count, last_prime)

def run():
    sieve = sieve_of_eratosthenes(1000000, lower_limit = 10)
    # builds masks
    bins = {}
    for i in range(1,7):
        all_bins = [bin(x)[2:] for x in range(1,2**i)]
        new = []
        # there have to be 3 digits to replace otherwise at least 3 would not be prime
        for j in all_bins:
            count = sum([1 for k in j if k == '1'])
            if count == 3:
                new.append(j)
        bins[i] = new
    
    for prime in sieve:
        binaries = bins[len(str(prime))-1]
        for b in binaries:
            res = number_primes(prime,b)
            if res[0] == 8:
                return res[1]

print(run())