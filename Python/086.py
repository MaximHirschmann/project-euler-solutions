from math import sqrt

z = 2
target = 1000000
count = 0

while count < target:
    z += 1
    for xy in range(3, 2*z + 1):
        root = sqrt(xy*xy + z*z)
        if root == int(root):
            if xy <= z:
                count += xy//2
            else:
                count += 1 + z - ((xy+1)//2)
print(z)