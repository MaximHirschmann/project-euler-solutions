def isLychrel(n):
    reverse = int(str(n)[::-1])
    for _ in range(51):
        n += reverse
        reverse = int(str(n)[::-1])
        if n == reverse:
            return False
    return True

print(sum([1 for i in range(10000) if isLychrel(i)]))