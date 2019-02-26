from math import gcd

numerator = 1
denominator = 1

for cancel in range(1, 10):
    for i in range(1, 10):
        for j in range(1, 10):
            num = 10*i + cancel
            denom = 10*cancel + j
            fract = num / denom
            simp = i / j    # fraction after digit 'cancel' is removed
            if fract < 1 and fract == simp:
                print(numerator, denominator)
                numerator *= num
                denominator *= denom

print(numerator, denominator)
result = denominator // gcd(numerator, denominator)
print(result)