# numerator(k) = numerator(k-1) + 2 * denominator(k-1)
# denominator(k) = numerator(k-1) + denominator(k-1)
count = 0
numerator = 1
denominator = 1
for _ in range(1000):
    old_n = numerator
    numerator += 2 * denominator
    denominator += old_n
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print(count)