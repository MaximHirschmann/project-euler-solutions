# hexagonal(n) equals triangle(2n)
def triangle(n):
    return n*(n-1)/2

def isPentagonal(n):
    # x = (1+(1+24*y)**(0.5))/6
    return (1+(1+24*n)**(0.5)) % 6 == 0

count = 0
i = 4
while count < 2:
    tri = triangle(i)
    if isPentagonal(tri):
        count += 1
    i += 2
print(int(triangle(i-2)))