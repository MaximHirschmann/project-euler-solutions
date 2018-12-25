# numerator(k) = numerator(k-1) + 2 * denominator(k-1)
# denominator(k) = numerator(k-1) + denominator(k-1)
count = 0
numerator, denominator = 1, 1
for _ in range(1000):
    numerator, denominator = numerator + 2*denominator, denominator + numerator
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print(count)