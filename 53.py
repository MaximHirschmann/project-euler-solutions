from math import factorial

# n!/(k!*(n-k)!)
def binomial_coefficent(n,k):
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

count = 0
for n in range(1,101):
    for r in range(1,n):
        if binomial_coefficent(n,r) > 1000000:
            count += 1
print(count)