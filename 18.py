with open("storage//18_pyramid.txt",'r') as f:
    pyramid = [[int(i) for i in line.replace("\n","").split(" ")] for line in f]

for i in reversed(range(2, len(pyramid)+1)):
    for j in range(len(pyramid[i-2])):
        if pyramid[i-1][j] > pyramid[i-1][j+1]:
            pyramid[i-2][j] += pyramid[i-1][j]
        else:
            pyramid[i-2][j] += pyramid[i-1][j+1]
    pyramid = pyramid[:i-1]

print(pyramid[0][0])