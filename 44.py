from Utils import save_time
from time import time

start = time()

def pentagonalNumber(n):
    return int((3*n*n-n)/2)

def isPentagonalNumber(n):
    # x = (1+(1+24*y)**(0.5))/6
    return (1+(1+24*n)**(0.5)) % 6 == 0

def find():
    pentagonal = []
    i = 1
    while True:
        pent = pentagonalNumber(i)
        for j in pentagonal:
            if isPentagonalNumber(abs(pent-j)) and isPentagonalNumber(pent+j):
                return (pent,j)
        pentagonal.append(pent)
        i += 1

res = find()
print(res[0]-res[1])
save_time(44, time()-start)