from Utils import divisor_function

def triangle_number(k):
    if k in table:
        return table[k]
    else:
        number = triangle_number(k-1) + k
        table[k] = number
        return number

table = {0: 0}
k = 1
while True:
    n = triangle_number(k)
    if divisor_function(n) > 500:
        print(n)
        break
    k += 1
