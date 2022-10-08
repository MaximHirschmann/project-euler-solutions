import sys
from sympy import isprime
from sympy.ntheory import factorint, primefactors
from collections import defaultdict

def save_time(project_number, new_time, path = sys.path[0]+"/times.txt"):
    with open(path,"r") as f:
        lines = f.read().split("\n")
        lines = [x.replace("s","").split(": ") for x in lines if len(x) != 0]
    dict = {int(i[0]):i[1] for i in lines}
    dict[project_number] = format(new_time,"f")
    with open(path,"w") as f:
        for key in sorted(dict.keys()):
            f.write(str(key)+": "+dict[key]+"s\n")

def isPrime(n):
    return isprime(n)

# returns unsorted list of primefactors
# if n is prime returns [n]
def primefactors_pollard_rho(n):
    if isPrime(n) == True:
        return [n]
    else:
        factors = []
        while n != 1:
            while True:
                factor = next_factor(n)
                if isPrime(factor) == True:
                    break
            factors.append(factor)
            n = int(n/factor)
        return factors

# pollard rho brent
def next_factor(n):
    from random import randint
    from fractions import gcd

    if n%2==0:
            return 2
    y,c,m = randint(1, n-1),randint(1, n-1),randint(1, n-1)
    g,r,q = 1,1,1
    while g==1:             
            x = y
            for _ in range(r):
                    y = ((y*y)%n+c)%n
            k = 0
            while (k<r and g==1):
                    ys = y
                    for _ in range(min(m,r-k)):
                            y = ((y*y)%n+c)%n
                            q = q*(abs(x-y))%n
                    g = gcd(q,n)
                    k = k + m
            r = r*2
    if g==n:
            while True:
                    ys = ((ys*ys)%n+c)%n
                    g = gcd(abs(x-ys),n)
                    if g>1:
                            break
        
    return g

def sieve_of_eratosthenes(limit,lower_limit=2,negatives = False):
    count,p=2,2
    numbers=[0,0]
    for a in range(2,limit+1):
        numbers.append(a)
    while p*p<limit:
        p=numbers[count]
        multiple=p+p 
        while multiple<=limit:
            numbers[multiple]=0
            multiple+=p
        count+=1
        while numbers[count]==0:
            count+=1
    numbers=list(filter(lambda a: a != 0, numbers))
    for i in range(len(numbers)):
        if numbers[i] >= lower_limit:
            numbers = numbers[i:]
            if negatives:
                neg = []
                for j in reversed(numbers):
                    neg.append(-j)
                numbers = neg + numbers
            return numbers
    return []
    
def divisor_function(n):
    return product(v+1 for v in factorint(n).values())

# returns sum of the proper divisors of a number n including n 
# uses the formulas:
# σ(p^a) = (p^(a+1) − 1)/(p − 1)
# σ(a×b×...)=σ(a)×σ(b)×...
def sum_of_proper_divisors(n):
    factors = factorint(n)
    return product([int((i[0]**(i[1]+1)-1)/(i[0]-1)) for i in factors.items()])

# euler totient function, number of numbers relative prime to n
def euler_totient(n):
    return int(product((1-(1/i)) for i in primefactors(n)) * n)

# returns unsorted list of integers which are divisors of n
def divisors_of(n):
    divisors = set()
    divisors.add(1)
    divisors.add(n)
    i = 2
    while i*i < n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(int(n/i))
        i += 1
    return list(divisors)

# counts length of the cycles of a fraction, n is the denominator, uses the concept of multiplicative order
# n has to be prime
# used for big numbers
def length_fraction_cycles_big(n):
    candidates = sorted(divisors_of(euler_totient(n)))
    for j in candidates:
        if 10**j % n == 1:
            return j

# uses same principle, but does not search for possible candidates, simply checks every number
def length_fraction_cycles(d):
    if d % 2 != 0 and d % 5 != 0 and d != 0 and d != 1:
        n = 1
        while (10**n - 1) % d != 0:
            n += 1
        return n

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
    
def isPandigital(s):
    numbers = {i:False for i in range(1,10)}
    for j in s:
        numbers[int(j)] = True
    return False not in numbers.values()

def isPalindrom(s):
    return s==s[::-1]

# returns index of value in a sorted list, if value not in list returns -1
def bisect(value,list):
    left = 0
    right = len(list) - 1
    while left <= right:
        check = (left+right)//2
        if list[check] == value:
            return check
        elif list[check] < value:
            left = check + 1
        else:
            right = check - 1
    return -1

def product(iterable):
    res = 1
    for i in iterable:
        res = res*i
    return res

def triangleNumber(n):
    return n*(n-1)/2

def isTriangleNumber(y):
    x = -0.5 + (0.25+2*y)**(1/2)
    return int(x) == x

def name_score(name):
    return sum(ord(i)-64 for i in name)

def pentagonalNumber(n):
    return int((3*n*n-n)/2)

def isPentagonalNumber(n):
    return (1+(1+24*n)**(0.5)) % 6 == 0

def digitsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def miller_rabin(n, bases):
    temp = n-1
    s = 0
    while temp%2 == 0:
        s += 1
        temp = temp//2
    d = (n-1)//(2**s)
    for a in bases:
        print(a)
        if pow(a,d,n) != 1:
            print("res", pow(a,d,n))
            print("first test true")
            if all(pow(a, (2**r)*d, n) != n-1 for r in range(s)):
                return False
            print("second test false")
        else:
            print("res", pow(a,d,n))
            print("first test false")
    return True
import sys

sys.setrecursionlimit(2000)
def poll_g(x, n):
    return (x*x+1)%n

def pollard_rho(n):
    x, y, d = 2, 2, 1
    while d==1:
        x = poll_g(x, n)
        y = poll_g(poll_g(y, n), n)
        d = gcd(abs(x-y), n)
        print(x,y,d)
    if d == n:
        return pollard_rho(n)
    else:
        return d

def primefactors_to_str(factors):
    res = ""
    for p, k in factors.items():
        if res != "":
            res += " * "
        if k > 1:
            res += str(p) + "^" + str(k)
        else:
            res += str(p)
    return res    