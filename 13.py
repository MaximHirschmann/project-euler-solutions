import sys

with open(sys.path[0]+"/storage/13.txt","r") as f:
    print(str(sum(map(int,f.read().split("\n"))))[:10])