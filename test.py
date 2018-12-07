from decimal import *
getcontext().prec = 1000
res = str(Decimal(2).sqrt())
for i in res:
    if i == '0':
        print(i, end='')
    else:
        print(i)
    