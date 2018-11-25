count = 0
for i in range(1,100):
    for j in range(1,10):
        if len(str(j**i)) == i:
            count += 1
print(count)