from Utils import sieve_of_eratosthenes
from time import process_time
from sympy import isprime

started=process_time()
# Set limit.  Value determined by experimentation.
LIMIT=40000

# Load list of PRIMES
PRIMES = sieve_of_eratosthenes(LIMIT)
PL = len(PRIMES)

pairs = {}

def tprime(x,y):
# Check two primes concatenated either way are prime.
# Creating a cache of results in dictionary reduces runtime by factor of 5
    assert x < y
    if (x,y) in pairs:
        return pairs[(x,y)]
    sx=str(x)
    sy=str(y)
    answer = isprime(int(sx+sy)) and isprime(int(sy+sx)) 
    pairs[(x,y)] = answer
    return answer

def answer():
    pairs.clear()
    
# Best answer so far
    best = LIMIT
    for i in range(PL):
        pi = PRIMES[i]
# Check that 5 values don't break best so far.  Repeated at each level below.
        if (pi+pi+pi+pi+pi) >= best : break
        for j in range(i+1,PL):
            pj=PRIMES[j]
            if (pi+pj+pj+pj+pj) >= best : break
# Check that current value at this level pairs with higher level(s). Repeated at each level below.
            if not tprime(pi,pj) : continue
            for k in range(j+1,PL):
                pk=PRIMES[k]
                if (pi+pj+pk+pk+pk) >= best : break
                if not (tprime(pi,pk) and tprime(pj,pk)) : continue
                for l in range(k+1,PL):
                    pl = PRIMES[l]
                    if (pi+pj+pk+pl+pl) >= best : break
                    if not (tprime(pi,pl) and tprime(pj,pl) and tprime(pk,pl)) : continue
                    for m in range(l+1,PL):
                        pm = PRIMES[m]
                        summ = pi+pj+pk+pl+pm
                        if summ >= best : break
                        if not (tprime(pi,pm) and tprime(pj,pm) and tprime(pk,pm) and tprime(pl,pm)) : continue
                        best = summ
                        bestl = (pi,pj,pk,pl,pm)
                        print(process_time()-started,best,bestl)

    print(process_time()-started,best,bestl)
answer()