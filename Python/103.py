def rec(n, l, sums, cur_min):
    length = len(l)
    res = None
    if length < n:
        lower_range = low if length == 0 else l[-1]+1
        upper_range = min(sum(l[:i+2])-sum(l[length-i:]) for i in range(length//2)) if length != 0 and length%2 == 0 else lim
        for a in range(lower_range, upper_range):
            new_sums = [a+i for i in sums] + [a]
            if any(i in sums for i in new_sums):
                continue
            opt = rec(n, l+[a], sorted(sums+new_sums), cur_min)
            if opt != None and sum(opt) < cur_min:
                res = opt
                cur_min = sum(opt)
        return res
    return l

n = 7
low = 20
lim = 50
cur_min = 1000
print("".join(str(i) for i in rec(n, [], [], cur_min)))