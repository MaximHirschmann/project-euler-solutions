from Utils import isPandigital

pandigital_multiples = []
max_3 = 0
max_4 = 0
for i in reversed(range(5000,10000)):
    s = str(i)+str(2*i)
    if i <= max_4:
        break
    if isPandigital(s):
        max_4 = i

for i in reversed(range(192,342)):
    s = str(i)+str(2*i)+str(3*i)
    if i <= max_3:
        break
    if isPandigital(s):
        max_3 = i

print(max(max_3, max_4))