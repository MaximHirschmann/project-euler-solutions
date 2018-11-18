combinations = set()
for a in range(2,101):
    for b in range(2,101):
        combinations.add(a**b)
print(len(combinations))