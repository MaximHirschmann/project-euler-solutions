def sum_squared_digits(n):
    result = 0
    while n:
        mod = n % 10
        result += mod*mod
        n = n//10
    return result

count = 0
arrives = {1:False, 89:True}

for x in range(1,568):
    s = str(x)
    while True:
        if int(s) in arrives:
            if arrives[int(s)]:
                arrives[x] = True
                count += 1
            else:
                arrives[x] = False
            break
        else:
            s = sum_squared_digits(int(s))

for i in range(568,10000000):
    if arrives[sum_squared_digits(i)]:
        count += 1
print(count)