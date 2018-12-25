from math import sqrt
from Utils import isTriangleNumber, name_score

def isTriangleWord(s):
    return isTriangleNumber(name_score(s))

with open('storage//42_words.txt','r') as f:
    words = eval(f.read())
print(sum([isTriangleWord(i) for i in words]))