from Utils import save_time
from time import time
from itertools import permutations

start = time()

# does not check for 5 because only gets divisible-by-5-numbers
def isdivisible(s):
    if s[0] != '0':
        if int(s[1]+s[2]+s[3]) % 2 == 0:
            # by 3
            if int(s[2]+s[3]+s[4]) % 3 == 0:
                # by 7
                if int(s[4]+s[5]+s[6]) % 7 == 0:
                    # by 11
                    if int(s[5]+s[6]+s[7]) % 11 == 0:
                        # by 13
                        if int(s[6]+s[7]+s[8]) % 13 == 0:
                            # by 17
                            if int(s[7]+s[8]+s[9]) % 17 == 0:
                                return True
    return False

digits = ('0','1','2','3','4','6','7','8','9')
perms = permutations(digits)
res = 0
for i in perms:
    num = ''.join(i[:5])+'5'+''.join(i[5:])
    if isdivisible(num):
        res += int(num)

print(res)
print(time()-start)
save_time(43,time()-start)