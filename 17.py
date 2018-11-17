from time import time
from Utils import save_time

start = time()
ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens = {0:0, 1:4, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
count = sum(ones.values())

for i in range(20,100):
    ten = int(i/10)
    one = i % 10
    length = tens[ten] + ones[one]
    ones[i] = length
    count += length

for i in range(100,1000):
    hundred = int(i/100)
    leftover = i % 100
    if leftover == 0:
        count += ones[hundred] + 7 + ones[leftover] # 7 because of: 'hundred'
    else:
        count += ones[hundred] + 10 + ones[leftover] # 10 because of: 'hundred and'

count += 11 # one thousand
print('Number: ', count)
end = time()
save_time(17,end-start)