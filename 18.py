with open("storage//18_pyramid.txt",'r') as f:
    pyramid = [[int(i) for i in line.replace("\n","").split(" ")] for line in f]

for i in reversed(range(1, len(pyramid))):
    for j in range(len(pyramid[i-1])):
        if pyramid[i][j] > pyramid[i][j+1]:
            pyramid[i-1][j] += pyramid[i][j]
        else:
            pyramid[i-1][j] += pyramid[i][j+1]

print(pyramid[0][0])