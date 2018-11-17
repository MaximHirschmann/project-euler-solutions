#from Utils import save_time
#from time import time

#start = time()
#straight forward
sum = 0
for i in range(1000):
  if i%3==0 or i%5==0:
    sum += i

print("Sum of all multiples: ", sum)
#end = time()
#save_time(1,end-start)