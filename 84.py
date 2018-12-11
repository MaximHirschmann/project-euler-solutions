import random

current = 0
sides = 4
count = {i:0 for i in range(40)}
limit = 100000

def roll_dice():
    s = 0
    for _ in range(3):
        d1 = random.randint(1, sides)
        d2 = random.randint(1, sides)
        s += d1 + d2
        if d1 != d2:
            return s
    return 0

def cc():
    global current
    card = random.randint(0,15)
    if card < 2:
        current = (0, 10)[card]

def ch():
    global current
    card = random.randint(0,15)
    if card < 10:
        if card == 6 or card == 7:
            if current == 7:
                current = 15
            elif current == 22:
                current = 25
            elif current == 36:
                current = 5
        elif card == 8:
            if current == 7 or current == 36:
                current = 12
            elif current == 22:
                current = 28
        elif card == 9:
            current = (current-3) % 40
        else:
            current = (0, 10, 11, 24, 39, 5)[card]

for i in range(limit):
    value = roll_dice()
    # three doubles
    if value == 0:
        current = 10
    else:
        current = (current + value) % 40
        # go to jail
        if current == 30:
            current = 10
        # community chest
        elif current == 2 or current == 17 or current == 33:
            cc()
        # chance
        elif current == 7 or current == 22 or current == 36:
            ch()
    count[current] += 1

squares = sorted(count.items(), key = lambda x: x[1], reverse = True)
res = ''
for i in squares[:3]:
    if len(str(i[0])) == 1:
        res += '0' + str(i[0])
    else:
        res += str(i[0])
print(res)