from math import log10 as log

with open('storage//99_pairs.txt','r') as f:
    pairs = [eval(line) for line in f.readlines()]

temp = [exp*log(base) for base, exp in pairs]

print(temp.index(max(temp))+1)