from collections import Counter

games = []
values = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
colors = {'C':0,'H':1,'D':2,'S':3}
with open('storage//54_poker.txt','r') as f:
    for line in f:
        cards = line.replace('\n','').split(' ')
        player1 = cards[:5]
        player2 = cards[5:]
        player1 = [[values[i[0]] for i in player1],[colors[i[1]] for i in player1]]
        player2 = [[values[i[0]] for i in player2],[colors[i[1]] for i in player2]]
        games.append([player1, player2])
# games = [game1,game2,game3]
# game1 = [player1, player2]
# player1 = [values, colors]
# values = {5:1, 6:2, 10:1, 11:1}  colors = {0:1,1:1,2:2}
def value(player):
    values = Counter(player[0])
    colors = Counter(player[1])
    
    isstraight = sorted(values.keys()) == list(range(min(values.keys()), max(values.keys())+1))
    samesuit = 5 in colors.values()
    # flush
    if samesuit and not isstraight:
        return 500 + max(values.keys())

    maxcounter = max(values.values())
    # High Card, Straight, Straight Flush, Royal Flush
    if maxcounter == 1:
        if isstraight:
            # Straight Flush, Royal Flush
            if samesuit:
                # Royal Flush
                if min(values.keys()) == 8:
                    return 900
                # Straight Flush
                else:
                    return 800 + max(values.keys())
            # Straight
            else:
                return 400 + max(values.keys())
        # High Card
        else:
            return max(values.keys())
    # One Pair, Two Pairs
    elif maxcounter == 2:
        pairs = [k for k,v in values.items() if v == 2]
        maxpair = max(pairs)
        numberofpairs = (len(pairs))
        # One Pair
        if numberofpairs == 1:
            return 100 + maxpair
        # Two Pairs
        else:
            return 200 + maxpair
        
    # Three of a kind, Full House
    elif maxcounter == 3:
        haspair = not all(v != 2 for v in values.values())
        # Full House
        if haspair:
            return 600 + max([k for k,v in values.items() if v == 3])
        # Three of a kind
        else:
            return 300 + max([k for k,v in values.items() if v == 3])

    # Four of a kind
    else:
        return 700 + max([k for k,v in values.items() if v == 4])
    return 0

print(sum(value(game[0]) > value(game[1]) for game in games))