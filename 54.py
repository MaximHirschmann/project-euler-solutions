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
# values = [1,5,2,7,5]  colors = [0,3,2,2,1]
def value(cards):
    values = Counter(cards[0])
    colors = Counter(cards[1])
    functions = [
        royalflush(values, colors),
        straightflush(values, colors),
        fourofakind(values, colors),
        fullhouse(values, colors),
        flush(values, colors),
        straight(values, colors),
        threeofakind(values, colors),
        twopairs(values, colors),
        onepair(values, colors),
        highestcard(values, colors),
    ]
    for i in functions:
        if i:
            return i
def royalflush():
    
count = 1
for game in games:
    if value(game[0]) > value(game[1]):
        count += 1
print(count)