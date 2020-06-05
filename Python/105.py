from itertools import combinations

# given a list returns if it is a secial sum set
def test(l):
    le = len(l)
    # check S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    s1, s2 = l[0], 0
    i = 1
    while i < le - i:
        s1 += l[i]
        s2 += l[-i]
        if s2 >= s1:
            return False
        i += 1

    # check If B contains more elements than C then S(B) > S(C).
    # goes through every combination if a sum appeared more than once return False
    length = 1
    while length <= le - length:
        sums = []
        for B in combinations(l, length):
            sums.append(sum(B)) 
        if len(sums) != len(set(sums)):
            return False
        length += 1
    return True

res = 0
with open("storage//105_sets.txt", "r") as f:
    for line in f.readlines():
        l = sorted(map(int, line.replace("\n", "").split(",")))
        if test(l):
            res += sum(l)
            
print(res)