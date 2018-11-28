used = []
append = used.append
pop = used.pop
solutions = []
min_i1 = 15

for a in range(1,6):
    append(a)
    for b in range(1,6):
        if b not in used:
            append(b)
            i1 = 14 - a - b
            if i1 not in used:
                append(i1)
                for c in range(1,6):
                    if c not in used:
                        append(c)
                        i2 = 14 - b - c
                        if i2 not in used:
                            append(i2)
                            for d in range(1,6):
                                if d not in used:
                                    append(d)
                                    i3 = 14 - c - d
                                    if i3 not in used:
                                        append(i3)
                                        for e in range(1,6):
                                            if e not in used:
                                                append(e)
                                                i4 = 14 - e - d
                                                i5 = 14 - a - e
                                                if i4 not in used:
                                                    append(i4)
                                                    if i5 not in used:
                                                        solutions.append("".join(map(str,[i1, a, b, i2, b, c, i3, c, d, i4, d, e, i5, e, a])))
                                                        if i1 < min_i1:
                                                            min_i1 = i1
                                                    pop(-1)
                                                pop(-1)
                                        pop(-1)
                                    pop(-1)
                            pop(-1)
                        pop(-1)
                pop(-1)
            pop(-1)
    pop(-1)
    
solutions.sort(reverse = True)
for i in solutions:
    if i[0] == str(min_i1):
        print(i)
        break