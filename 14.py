def collatz_length(n):
    save = n
    count = 0
    while True:
        if n in table:
            length = table[n] + count
            table[save] = length
            return length
        else:
            if n%2 == 0:
                n = int(n/2)
            else:
                n = 3*n+1
            count += 1

table = {1:1}
max = 0
for i in range(1,1000000):
    length = collatz_length(i)
    if length > max:
        max = length
        index = i
print(index)
