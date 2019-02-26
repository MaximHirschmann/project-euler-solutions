from itertools import combinations, product

def check(cube1, cube2):
    pairs = list(product(cube1, cube2))
    for i in squares:
        test = False # if pairs includes one of the ways to represent the squared number
        for j in i:
            if j in pairs:
                test = True
                break
        if not test:
            return False
    return True

squares = (
    (('0','1'),('1','0')),
    (('0','4'),('4','0')),
    (('0','9'),('9','0'),('0','6'),('6','0')),
    (('1','6'),('6','1'),('1','9'),('9','1')),
    (('2','5'),('5','2')),
    (('3','6'),('6','3'),('3','9'),('9','3')),
    (('4','9'),('9','4'),('4','6'),('6','4')), # 7^2 and 8^2
    (('8','1'),('1','8')))

nums = [str(i) for i in range(10)]
comb = list(combinations(nums, 6))
count = 0
for i in range(len(comb)-1):
    for j in range(i+1, len(comb)):
        if check(comb[i], comb[j]):
            count += 1
print(count)