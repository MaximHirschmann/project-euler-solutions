import decimal

def sum_digits(s):
    return sum(map(int, s))
    
decimal.getcontext().prec = 100
squares = [i*i for i in range(11)]

res = 0
nums = []
for i in range(101):
    if i in squares:
        continue
    dec = decimal.Decimal(i).sqrt()
    res += sum_digits(str(dec).replace('.',''))
print(res)