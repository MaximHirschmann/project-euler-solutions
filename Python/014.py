import time
start = time.time()
def collatz_length(n):
    count = 0
    sequence = []
    while True:
        if n in table:
            length = table[n] + count
            for i in range(len(sequence)):
                table[sequence[i]] = length-i
            return length
        else:
            sequence.append(n)
            if n%2 == 0:
                n = n//2
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
print(time.time()-start)