# inspired by https://blog.dreamshire.com/project-euler-88-solution/
def generate_factors(product = 1, s = 1, number_factors = 1, start = 2):
    k = product - s + number_factors
    if k < limit:
        if product < factors[k]:
            factors[k] = product
        for i in range(start, (limit//product)*2 + 1):
            generate_factors(product = product*i, 
            s = s+i, number_factors = number_factors+1, start = i)

limit = 12000
factors = {i:2*limit for i in range(1, limit*2 + 1)}
generate_factors()
print(sum(set(factors.values())) - 2*limit)