from sympy import primefactors

factors = primefactors(600851475143)
print(max(factors))