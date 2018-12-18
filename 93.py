from operator import add, sub, mul
from numpy import divide # to avoid zero division errors
from itertools import combinations, permutations, product

def length(digits):
    perms = permutations(digits, 4)
    i = 1
    while True:
        canbuild = False
        for num in perms:
            a,b,c,d = num[0],num[1],num[2],num[3]
            for op in operations:
                # check ways to place brackets
                if ((op[2](op[1](op[0](a, b), c), d) == i) 
                or (op[2](op[0](a, op[1](b, c)), d) == i)
                or (op[1](op[0](a, b), op[2](c, d)) == i)
                or (op[0](a, op[2](op[1](b, c), d)) == i)
                or (op[1](op[0](a, b), op[2](c, d)) == i)):
                    canbuild = True
                    break
            if canbuild:
                break
        if not canbuild:
            return i-1
        i += 1

nums = list(combinations(range(1, 10), 4))
operations = list(product([add, sub, mul, divide], repeat = 3))

max = 0
for num in nums:
    l = length(num)
    if l > max:
        max = l
        max_num = num
print(''.join(map(str, max_num)))