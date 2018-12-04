# using the partition function http://mathworld.wolfram.com/PartitionFunctionP.html
def partition(n):
    if n < 0:
        return 0
    if n in table:
        return table[n]
    result = 0
    k = 1
    while True:
        sign = ( -1 ) ** ( k + 1 )
        num1 = int( k * ( k * 3 - 1 )  / 2)
        num2 = int( k * ( k * 3 + 1 )  / 2)
        if n < num1 and n < num2:
                break
        result += sign * ( partition( n - num1 ) + partition( n - num2 ))
        k += 1
    mod = result % 1000000
    table[n] = mod
    return mod

table = {0:1}
i = 0
p = 1
while p % 1000000 != 0:
    i += 1
    p = partition(i)
print(i)