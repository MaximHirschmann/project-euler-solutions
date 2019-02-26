def fibonacci(n):
    if n in table:
        return table[n]
    else:
        fib = fibonacci(n-1)+fibonacci(n-2)
        table[n] = fib
        return fib

table = {1:1,2:1}
i = 3
while True:
    if len(str(fibonacci(i))) == 1000:
        print(i)
        break
    i += 1