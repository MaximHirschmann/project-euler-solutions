from Utils import isPandigital

products = set()
for small in range(1,100):
    for big in range(small,10000):
        product = small * big
        if len(str(product)) == 4 and isPandigital(str(small)+str(big)+str(product)):
            products.add(product)

print(sum(products))