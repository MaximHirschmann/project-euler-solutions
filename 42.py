from math import sqrt

def isTriangleWord(s):
    return isTriangle(name_score(s))

def isTriangle(y):
    x = -0.5 + sqrt(0.25+2*y)
    if int(x) == x:
        return True
    return False

def name_score(name):
    return sum(ord(i)-64 for i in name)

with open('storage//42_words.txt','r') as f:
    words = eval(f.read())
print(sum([1 for i in words if isTriangleWord(i)]))