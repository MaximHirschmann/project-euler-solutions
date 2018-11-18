from sympy.ntheory import primefactors

def length4(n):
    if n in table:
        return table[n]
    else:
        res = len(primefactors(n)) == 4
        table[n] = res
        return res

table = {}
i = 0
while True:
    check = True
    for j in range(i,i+4):
        if not length4(j):
            check = False
            break
    if check:
        print(i)
        break
    i += 1