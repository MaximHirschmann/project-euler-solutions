from time import time

start = time()

def isBouncy(n):
    digits = list(str(n))
    s = sorted(digits)
    return digits != s and digits != s[::-1]

percentage = 0.99

bouncy = 0
i = 1
while bouncy / i < percentage:
    i += 1
    if isBouncy(i):
        bouncy += 1
    
print(i)

print(time() - start)