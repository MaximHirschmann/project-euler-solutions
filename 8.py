import sys

with open(sys.path[0]+"/storage/8.txt") as f:
    number = f.read().replace("\n","")

max = 0
adjacent_digits = 13
for i in range(len(number)-adjacent_digits):
    product = 1
    for j in range(i,i+adjacent_digits):
        product *= int(number[j])
    if product > max:
        max = product
print(max)