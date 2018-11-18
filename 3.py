from sympy import primefactors

factors = primefactors(600851475143)
print("Largest prime factor:", max(factors))