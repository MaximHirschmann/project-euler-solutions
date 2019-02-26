# returns n-th number of the spiral
def spiral(n):
    if n in table:
        return table[n]
    res = spiral(n-1) + 2*(int((n-1)/4))+2
    table[n] = res
    return res

table = {0:1}
d = 1001
print(sum(spiral(i) for i in range(2*d-1)))