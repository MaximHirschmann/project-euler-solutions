def isLychrel(n):
    reverse = int(str(n)[::-1])
    for _ in range(50):
        n += reverse
        reverse = int(str(n)[::-1])
        if n == reverse:
            return False
    return True

print(sum(isLychrel(i) for i in range(10000)))