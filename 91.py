from Utils import save_time
from time import time

start = time()

gridsize = 50
count = 0
for x1 in range(gridsize+1):
    for y1 in range(gridsize+1):
        if not (x1 == 0 and y1 == 0):
            for x2 in range(gridsize+1):
                for y2 in range(y1,gridsize+1):
                    if not (x2 == 0 and y2 == 0) and (y2 != y1 or x2 > x1):
                        # side lengths squared
                        sides = [
                            x1**2 + y1**2, 
                            (x2 - x1)**2 + (y2 - y1)**2, 
                            x2**2 + y2**2
                        ]
                        sides.sort()
                        # check if a**2 + b**2 = c**2
                        if sides[0] + sides[1] == sides[2]:
                            count += 1
print(count)
save_time(91, time()-start)
