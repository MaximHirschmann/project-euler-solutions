import numpy

def multiply(n, arr):
    carry = 0
    length = arr.size
    for i in range(length):
        p = arr[i]*n + carry
        arr[i] = p%10
        carry = p//10
    
    while carry:
        arr[length] = carry%10
        carry = carry//10
        length += 1 

arr = numpy.zeros(400, dtype=numpy.byte)
arr[0] = 1
for i in range(1000):
    multiply(2, arr)