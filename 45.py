# hexagonal(n) equals triangle(2n)
from Utils import triangleNumber, isPentagonalNumber

count = 0
i = 4
while count < 2:
    tri = triangleNumber(i)
    if isPentagonalNumber(tri):
        count += 1
    i += 2
print(int(triangleNumber(i-2)))