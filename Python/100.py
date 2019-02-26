# formular from https://www.alpertron.com.ar/QUAD.HTM
# where the equation is n² - n - 2b² + 2b = 0
n = 21
b = 15

while True:
    n, b = 3*n + 4*b - 3, 2*n + 3*b - 2
    if n > 10**12:
        print(b)
        break