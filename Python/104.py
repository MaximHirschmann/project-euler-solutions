import math

def fib_first_digits(n):
    l = n * log_phi - log_root
    l = l - int(l) + 8
    return str(10**l)[:9]

def isPandigital(nums):
    return "".join(sorted(nums)) == "123456789"

root = math.sqrt(5)
log_root = math.log10(root)
log_phi = math.log10((1+root)/2)

i = 3
last = 1
last2 = 1
while True:
    ending = (last + last2)%(10**9)
    if isPandigital(str(ending)) and isPandigital(fib_first_digits(i)):
        print(i)
        break
    last, last2 = ending, last
    i += 1