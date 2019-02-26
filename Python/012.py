from Utils import divisor_function

last = 0
k = 1
while True:
    tri = last + k
    if divisor_function(tri) > 500:
        print(tri)
        break
    last = tri
    k += 1
