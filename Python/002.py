last = 1
lastlast = 1

count, sum = 1, 0
while True:
    value = last + lastlast
    if value >= 4000000:
        break
    if value%2 == 0:
        sum += value
    last, lastlast = value, last
    count += 1

print(sum)