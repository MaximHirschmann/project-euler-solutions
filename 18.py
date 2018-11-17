from Utils import save_time
from time import time

start = time()

pyramid = []
with open("storage//18_pyramid.txt",'r') as f:
    for line in f:
        temp = line.replace("\n","").split(" ")
        for x in range(len(temp)):
            temp[x] = int(temp[x])
        pyramid.append(temp)

def printpyramid(pyramid):
    print("\n")
    for i in pyramid:
        print(i)

printpyramid(pyramid)
i = len(pyramid)
while i > 1:
    for j in range(len(pyramid[i-2])):
        if pyramid[i-1][j] > pyramid[i-1][j+1]:
            pyramid[i-2][j] += pyramid[i-1][j]
        else:
            pyramid[i-2][j] += pyramid[i-1][j+1]
    pyramid = pyramid[:len(pyramid)-1]
    i = len(pyramid)
    printpyramid(pyramid)

print('Number:', pyramid[0][0])
end = time()
save_time(18,end-start)
