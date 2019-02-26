from Utils import product

with open("storage//8.txt") as f:
    number = f.read().replace("\n","")

max = 0
adjacent_digits = 13
for i in range(len(number)-adjacent_digits):
    prod = product(int(number[j]) for j in range(i, i+adjacent_digits))
    if prod > max:
        max = prod
print(max)
