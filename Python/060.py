from Utils import sieve_of_eratosthenes
from sympy import isprime

# checks if two numbers concatenated are primes in both ways, returns True if satisfies condition
def check(x,y):
    if (x,y) in pairs:
        return pairs[(x,y)]
    sx, sy = str(x), str(y)
    answer = isprime(int(sx+sy)) and isprime(int(sy+sx)) 
    pairs[(x,y)] = answer
    return answer

pairs = {}
sieve = sieve_of_eratosthenes(10000)
res = 40000 # current minmum, in the beginning random high number
length = len(sieve)
# i1, i2, i3, i4, i5 are indices
# a, b, c, d, e are numbers
for i1, a in enumerate(sieve):
    # a has to be smaller than one-fifth of the current minimum
    if a*5 >= res:
        break
    for i2 in range(i1+1, length):
        b = sieve[i2]
        # b has to be smaller than one-fourth of the current minimum - a
        if a + 4*b >= res:
            break
        if not check(a,b):
            continue
        for i3 in range(i2+1, length):
            c = sieve[i3]
            # c has to be smaller than one-third of the current minimum-a-b
            if a + b + 3*c >= res:
                break
            if not (check(a,c) and check(b,c)):
                continue
            for i4 in range(i3+1, length):
                d = sieve[i4]
                # d has to be smaller than one-half of the current minimum-a-b-c
                if a + b + c + 2*d >= res:
                    break
                if not (check(a,d) and check(b,d) and check(c,d)):
                    continue
                for i5 in range(i4+1, length):
                    e = sieve[i5]
                    if a+b+c+d+e >= res:
                        break
                    if not (check(a,e) and check(b,e) and check(c,e) and check(d,e)):
                        continue
                    res = a+b+c+d+e
print(res)