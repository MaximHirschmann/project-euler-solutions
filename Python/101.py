import numpy as np

degree_total = 10
# generate first 10 terms of series
series = [sum((-i)**j for j in range(11)) for i in range(1, degree_total  + 1)]
res = 0

for degree in range(1, degree_total + 1):
    # solve linear equations using numpy's solve function A: left side, B: right side, 
    left = np.array([[i**j for j in range(degree)] for i in range(1,degree+1)])
    right = np.array(series[:degree])
    coefficients = np.linalg.solve(left, right) 
    # generate next term of the series according to the polynomial coefficients and add to the result
    res += int(round(sum(coef*(degree+1)**i for i, coef in enumerate(coefficients))))

print(res)