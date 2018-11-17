from Utils import save_time
from time import time
from Utils import sieve_of_eratosthenes
from itertools import product
from sympy import isprime

start = time()

# replace 1's keep 0's
def count(perm):
    max = 0
    max_num = 0
    digits = ("1","2","3","4","5","6","7","8","9","0")
    length = sum([1 for j in perm if j == '0'])
    if length == len(perm):
        return (0,0)
    for numbers in perms_digits[length]:
        res = 0
        for digit in digits:
            # TODO change
            new = ''
            count2 = 0
            for i in range(len(perm)):
                if perm[i] == '0':
                    new += numbers[count2]
                    count2 += 1
                else: # perm[i] == '1'
                    new += digit
            if isprime(int(new)):
                res += 1
        if res > max:
            max = res
            max_num = numbers
    return (max, max_num)

def run():
    for perms in perms_all.values():
        for perm in perms:
            res = count(perm)
            print(res, perm)
            if res[0] == 8:
                num = ''
                count2 = 0
                for j in perm:
                    if j == '0':
                        num += res[1][count2]
                        count2 += 1
                    else:
                        num += '1'
                return num

digits = ("1","2","3","4","5","6","7","8","9","0")
perms_all = {i:product(('0','1'), repeat = i) for i in range(1,7)}
perms_digits = {i:list(product(digits, repeat = i)) for i in range(7)}
print(run())
save_time(51,time()-start)