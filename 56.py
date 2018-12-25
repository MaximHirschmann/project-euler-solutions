from Utils import digitsum

print(max(digitsum(a**b) for a in range(100) for b in range(100)))