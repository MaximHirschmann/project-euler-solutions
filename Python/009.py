from Utils import product

def find_triplet(u):
    for a in range(1,int(u/3)):
        b = (-2*a*u + u*u)/(-2*a + 2*u)
        if int(b) == b:
            return [a,b,u-a-b]

triplet = find_triplet(1000)
print(product(int(i) for i in triplet))
