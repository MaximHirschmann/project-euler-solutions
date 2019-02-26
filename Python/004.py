from Utils import isPalindrom

res = 0
for i in reversed(range(100,1000)):
    if i * 999 <= res:
        break
    for j in reversed(range(i,1000)):
        product = i * j
        if product <= res:
            break
        if isPalindrom(str(product)):
            res = product
print(res)