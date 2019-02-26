with open('storage//22_names.txt','r') as f:
    names= sorted(list(eval(f.read())))

def name_score(name, index):
    return sum(ord(i)-64 for i in name) * (index+1)

res = 0
for i in range(len(names)):
    res += name_score(names[i], i)
print(res)