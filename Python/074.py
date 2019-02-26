from math import factorial

def sum_factorial_digits(n):
    return sum(factorials[i] for i in str(n))

factorials = {str(i): factorial(i) for i in range(10)}
lengths = {}
count = 0
for i in range(1, 1000000):
    res = i
    chain = [i]
    length = 1
    while True:
        res = sum_factorial_digits(res)
        if res in lengths:
            length += lengths[res]
            break
        else:
            if res in chain:
                break
            chain.append(res)
            length += 1
    for index, num in enumerate(chain):
        lengths[num] = length - index
    if length == 60:
        count += 1
print(count)