# the problem can be expressed as how many ways are there to choose the twenty down-moves from fourty moves
from math import factorial

# n!/(k!*(n-k)!)
def binomial_coefficent(n,k):
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

print(binomial_coefficent(40,20))
