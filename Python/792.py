# NOT FINISHED

from time import time
import functools
import scipy
import bisect
from math import factorial
from sympy import factorint
from tabulate import tabulate
import scipy.special as sc


# bin(2k, k) 
def bin_helper(k):
    p1 = 1
    p2 = 1
    for i in range(1, k+1):
        p1 *= i
    for i in range(k+1, 2*k+1):
        p2 *= i
    return p2 // p1
    

@functools.lru_cache(None)
def rec(n):
    if n == 0:
        return 1
    else:
        return rec(n-1) * (4 * n - 2) // n

mem = {0: 0}
in_mem = [0]
def S(n):
    if n in in_mem:
        return mem[n]
    idx = bisect.bisect_right(in_mem, n) - 1
    val = in_mem[idx]
    s = mem[val]
    for i in range(val+1, n+1):
        s += ((-2) ** i) * rec(i)
    in_mem.append(n)
    mem[n] = s
    return s

def ny_2(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            count += 1
            n = n // 2
        else:
            return count
    return count
  
@functools.lru_cache(None)  
def u(n):
    return ny_2(3 * S(n) + 4)
    
def U(N):
    s = 0
    for n in range(1, N+1):
        s += u(n**3)
    return s


class Bin:
    def __init__(self, binary, shift):
        if binary == "0b0":
            self.binary = binary
            self.shift = shift
        else:
            count = 0
            for i in reversed(range(len(binary))):
                if binary[i] == "0":
                    count += 1
                else:
                    break
            
            if count != 0:
                self.binary = binary[:-count]
            else:
                self.binary = binary
            self.shift = shift + count
        
    def __add__(self, otherBin):
        s = ""
        if self.shift < otherBin.shift:
            return otherBin + self
        move = self.binary + "0" * (self.shift - otherBin.shift)
        dec_res = int(move, 2) + int(otherBin.binary, 2)
        new_bin = bin(dec_res)
        res = Bin(new_bin[:], otherBin.shift)
        return res

    def __repr__(self) -> str:
        #return str((int(self.binary, 2) * 2**self.shift - 4) // 3 ) # decimal num
        return self.binary + " * 2^" + str(self.shift)
    
def S_naive(n):
    s = 0
    table = []
    for k in range(1, n+1):
        add = (-2) ** k * rec(k)
        #table.append(["k = " + str(k), bin(add)])
        s += add
    #print(tabulate(table, stralign="right"))
    return s   
    
mem2 = {1: Bin(bin(-8), 0) }
calculated2 = [1]
# 3 * S(n) + 4
@functools.lru_cache(None)
def S3(n):
    if n in mem2:
        return mem2[n]
    
    idx = bisect.bisect_right(calculated2, n) - 1
    val = calculated2[idx]
    s = mem2[val]
    
    for i in range(val+1, n+1):
        s += Bin(bin((-1)**i * 3 * rec(i)), i)
    
    calculated2.append(n)
    mem2[n] = s
    
    return s
    
def u2(n):
    s = S3(n)
    return s.shift
    
def U2(N):
    s = 0
    for n in range(1, N+1):
        s += u2(n**3)
    return s

start = time()

table = []
for i in range(1000,2000):
    table.append([u2(i)])
    
# table = []
# for i in range(1, 20):
#     # table.append([i, (-2)**i * rec(i), bin((-2)**i * rec(i))])
#     table.append([i, ny_2(rec(i)), ny_2(3 * S(i) + 4)])
    
print(tabulate(table, stralign="right"))


print(time()-start, "s")
