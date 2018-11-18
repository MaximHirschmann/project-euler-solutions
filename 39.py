# right triangle
def sides_with_perimeter(p):
    count = 0
    a = 1
    b = 2
    while a < b:
        b = (2*a*p-p*p)/(2*a-2*p)
        if b == int(b):
            count += 1
        a += 1
    return count

max_length = 0
max_index = 0
for i in range(12,1001):
    length = sides_with_perimeter(i)
    if length > max_length:
        max_length = length
        max_index = i

print('The number',max_index,'with a length of',max_length)