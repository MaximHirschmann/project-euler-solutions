from collections import Counter

cubes = [x*x*x for x in range(10000)]
# digits of the cubes
digits = [tuple(sorted([int(j) for j in str(i)])) for i in cubes]

# counts number of appearences of same digits
count = Counter(digits)
for k,v in count.items():
    if v == 5:
        res = k
        break
# prints smallest number with those digits
for i in range(len(digits)):
    if digits[i] == res:
        print(cubes[i])
        break