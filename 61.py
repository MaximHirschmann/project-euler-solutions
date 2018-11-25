def get_length(num):
    types = [num[0]]
    chain = [num]
    for a in relation[num]:
        if a in chain or a[0] in types:
            continue
        types.append(a[0])
        chain.append(a)
        for b in relation[a]:
            if b in chain or b[0] in types:
                continue
            types.append(b[0])
            chain.append(b)
            for c in relation[b]:
                if c in chain or c[0] in types:
                    continue
                types.append(c[0])
                chain.append(c)
                for d in relation[c]:
                    if d in chain or d[0] in types:
                        continue
                    types.append(d[0])
                    chain.append(d)
                    for e in relation[d]:
                        if e in chain or e[0] in types:
                            continue
                        types.append(e[0])
                        chain.append(e)
                        for f in relation[e]:
                            if f == num:
                                return [num,a,b,c,d,e,f,]
                        types.pop(-1)
                        chain.pop(-1)
                    types.pop(-1)
                    chain.pop(-1)
                types.pop(-1)
                chain.pop(-1)
            types.pop(-1)
            chain.pop(-1)
        types.pop(-1)
        chain.pop(-1)
    return 0

nums = [
    [(x*x + x)//2 for x in range(45,141)],
    [x*x for x in range(32,100)],
    [(3*x*x - x)//2 for x in range(26,82)],
    [2*x*x - x for x in range(23,71)],
    [(5*x*x - 3*x)//2 for x in range(21,64)],
    [3*x*x -2*x for x in range(19,59)]
]

relation = {}
# generate all keys
for i, a in enumerate(nums):
    for b in a:
        relation[(i, b%100)] = []
# generate all values
for own_type, a in enumerate(nums):
    for b in a:
        for type_pair in range(6):
            if own_type != type_pair:
                if (type_pair, b // 100) in relation:
                    relation[(type_pair, b // 100)] += [(own_type, b%100)]

for k, v in relation.items():
    res = get_length(k)
    if res:
        # get sum of numbers
        print(sum(int(str(res[i-1][1]) + str(res[i][1])) for i in reversed(range(1, len(res)))))
        break