nums = [
    [(x*x + x)//2 for x in range(45,141)],
    [x*x for x in range(32,100)],
    [(3*x*x - x)//2 for x in range(26,82)],
    [2*x*x - x for x in range(23,71)],
    [(5*x*x - 3*x)//2 for x in range(21,64)],
    [3*x*x -2*x for x in range(19,59)]
]

cycle_length = 6
relation = {}
# generate all keys
for i, a in enumerate(nums):
    for b in a:
        relation[(i, b%100)] = []
# generate all values
for own_type, values in enumerate(nums):
    for v in values:
        for partner_type in range(cycle_length):
            if own_type != partner_type:
                partner = (partner_type, v // 100)
                if partner in relation:
                    relation[partner].append((own_type, v%100))

def solve(types, chain):
    ''' 
    Solves for the chain of a cycle of the length cycle_length given a first entry in types and chain\n
    Returns the chain if a solution is found otherwise False\n
    Example:
        result = solve([2], [86])
    '''
    if len(chain) > cycle_length:
        return False
    # required length, includes all types, if the first value is the next of the last
    if (len(chain) == cycle_length and all(i in types for i in range(cycle_length)) and (types[0],chain[0]) in relation[(types[-1],chain[-1])]):
        return chain
    for type, num in relation[(types[-1],chain[-1])]:
        if type not in types or num not in chain:
            res = solve(types+[type], chain+[num])
            if res:
                return res
    return False

def run():
    for v in relation.values():
        for type, num in v:
            res = solve([type],[num])
            if res:
                return sum(res)*100 + sum(res)

print(run())