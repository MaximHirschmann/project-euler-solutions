from Utils import save_time
from time import time

start = time()

def isPalindrom(s):
    if(s==s[::-1]):
      return True
    return False

print(sum([i for i in range(1,1000000) if (isPalindrom(str(i)) and isPalindrom(bin(i)[2:]))]))

save_time(36,time()-start)