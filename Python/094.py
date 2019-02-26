# using Pells equation
limit = 1000000000
x, y = 7, 4
res = 0

while True:
    a = (2*x - 1)/3
    area = (y * (x-2))/3
    if a*3 > limit:
        break
    if a == int(a) and area == int(area):
        res += 3*a + 1

    a = (2*x + 1)/3
    area = (y * (x+2))/3
    if a == int(a) and area == int(area):
        res += 3*a - 1
    
    x, y = 2*x + y*3, 2*y + x

print(int(res))