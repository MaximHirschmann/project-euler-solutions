import datetime
from Utils import save_time
from time import time

start = time()

count=0
for year in range(1901,2001):
    for month in range(1,13):
        if datetime.datetime(year,month,1).weekday()==6:
            count+=1
print(count)
save_time(19,time()-start)