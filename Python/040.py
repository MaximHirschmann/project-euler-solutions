from Utils import product

s = ""
length = 0
number = 0
while length <= 100000:
    s += str(number)
    length += len(str(number))
    number += 1

print(product(int(s[10**i]) for i in range(6)))