from itertools import permutations

# does not check for 5 because only gets divisible-by-5-numbers
def isdivisible(s):
    if s[0] == '0':
        return False
    divisors = [2, 3, 5, 7, 11, 13, 17]
    
    for i in range(7):
        if int(s[i+1] + s[i+2] + s[i+3]) % divisors[i] != 0:
            return False
    return True

digits = ('0','1','2','3','4','6','7','8','9')
perms = permutations(digits)
res = 0
for i in perms:
    num = ''.join(i[:5])+'5'+''.join(i[5:])
    if isdivisible(num):
        print(num)
        res += int(num)

print(res)