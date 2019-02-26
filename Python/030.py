def sum_of_power_digits(n, power):
    digits = tuple(sorted([int(i) for i in str(n)]))
    if digits in table:
        return table[digits]
    res = sum([i**power for i in digits])
    table[digits] = res
    return res

table = {}
print(sum(i for i in range(10,354294) if i == sum_of_power_digits(i,5)))