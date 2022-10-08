# NOT FINISHED

from collections import defaultdict
import functools
import itertools
from tabulate import tabulate
from time import time
from sympy import factorint

start = time()

n = 4
s = 6

def other(player):
    return -player

def filter_deck(visible, deck):
    smallest_of_suit = [n] * s
    for num, suit in visible:
        smallest_of_suit[suit] = min(smallest_of_suit[suit], num)
    
    new_deck = []
    for num, suit in deck:
        if num <= smallest_of_suit[suit]:
            continue
        else:
            new_deck.append((num, suit))
    return new_deck
    
def filter_visible(visible, deck):
    biggest_of_suit = [-1] * s
    for num, suit in deck:
        biggest_of_suit[suit] = max(biggest_of_suit[suit], num)
        
    new_visible = []
    for num, suit in visible:
        if num >= biggest_of_suit[suit]:
            continue
        else:
            new_visible.append((num, suit))
    return new_visible
    
# players turn
def rec(visible, deck, player = 1, depth = 0):
    if visible == [(0, 1), (1, 0)]:
        pass
    if visible == [] or deck == []:
        return other(player)

    #deck = filter_deck(visible, deck)
    #visible = filter_visible(visible, deck)
    
    move_available = False
    for i in range(len(deck)):
        num1, suit1 = deck[i]
        for j in range(len(visible)):
            num2, suit2 = visible[j]
            if suit2 != suit1 or num2 > num1: # you cant put that card on top of the other one
                continue
            new_visible = [(num1, suit1) if k == j else visible[k] for k in range(len(visible))]
            new_deck = [deck[k] for k in range(len(deck)) if k != i ]
            #print("   " * depth, (num1, suit1), "on", (num2, suit2))
            res = rec(new_visible, new_deck, other(player), depth + 1)
            if res == player:
                return player

    return other(player)

@functools.lru_cache(None)
def rec3(higher, depth = 0):
    higher = tuple(i for i in higher if i != 0)
    
    if higher == ():
        return -1
    
    grouped = defaultdict(int)
    for i in higher:
        grouped[i] += 1
    
    g = tuple(sorted(grouped.items()))
    
    # iterate over moves
    for v, _ in g:
        for i in range(v):
            new = []
            once = False
            for elem in higher:
                if elem == v:
                    if once:
                        new.append(elem - 1)
                    else:
                        new.append(i)
                        once = True
                elif elem < v:
                    if i < elem:
                        new.append(elem - 1)
                    else:
                        new.append(elem)
                else:
                    new.append(elem - 1)
            new.sort()
            new = tuple(new)
            res = rec3(new, depth + 1)
            if res == -1:
                return 1
    
    return -1

def filter_zeros(higher):
    new = []
    for suit in higher:
        new2 = []
        for elem in suit:
            if elem != 0:
                new2.append(elem)
        if new2:
            new.append(tuple(new2))
    return tuple(new)

def base2(higher):
    new = []
    for suit in higher:
        highest = max(suit)
        c = 0
        for i in suit:
            if i == highest:
                c += 1
        c = min(c, 2)
        new_suit = [highest for _ in range(c)]
        new.append(tuple(new_suit))
    return tuple(new)

mem = {}
# input of form ((2, 3, 4), (1, 2), (2))
def rec3_2(higher):
    higher = filter_zeros(higher)
    if higher in mem:
        return mem[higher]
    if higher == ():
        return -1
    
    for idx, suit in enumerate(higher):
        last = None
        for i in suit:
            if i == last:
                continue
            last = i
            
            for value in range(i):
                new = []
                once = False
                for elem in suit:
                    to_add = 0
                    if elem == i:
                        if once:
                            to_add = elem - 1
                        else:
                            to_add = value
                            once = True
                    elif elem < i:
                        if value < elem:
                            to_add = elem - 1
                        else:
                            to_add = elem
                    else:
                        to_add = elem - 1
                    
                    if to_add != 0:
                        new.append(to_add)
                new.sort()
                new = tuple(new)
                new2 = [higher[j] if j != idx else new for j in range(len(higher))]
                new2.sort()
                #print(new2)
                res = rec3_2(tuple(new2))
                if res == -1:
                    mem[higher] = 1
                    return 1
    mem[higher] = -1
    return -1
    
def who_wins(visible, deck, player = 1):
    ret = []
    for suit in range(s):
        new_visible = [(num1, suit1) for num1, suit1 in visible if suit1 == suit]
        new_deck = [(num1, suit1) for num1, suit1 in deck if suit1 == suit]
        res = who_wins_one_suite(new_visible, new_deck, player)
        match res:
            case (False, True):
                new = 0
            case (True, False):
                new = 1
            case (True, True):
                new = 2
        
        ret.append(new)
        
    return ret

def split_to_result(splitted):
    count = [0, 0, 0]
    for i in splitted:
        count[i] += 1
    
    if count[1] % 2 == 0 and count[2] % 2 == 0:
        return -1
    else:
        return 1

def who_wins_one_suite(visible, deck, player = 1):
    # can i force a win?
    win = winner_best_play(visible, deck) == 1
    # can i force a loss
    loss = winner_worst_play(visible, deck) == -1
    
    return (win, loss)

def winner_best_play(visible, deck, player=1):
    if visible == [] or deck == []:
        return other(player)
    
    for card_chosen in deck:
        for stack_chosen in visible:
            if stack_chosen[1] != card_chosen[1] or stack_chosen[0] > card_chosen[0]: # you cant put that card on top of the other one
                continue
            new_visible = [card_chosen if card == stack_chosen else card for card in visible]
            new_deck = [card for card in deck if card != card_chosen]
            res = winner_best_play(new_visible, new_deck, other(player))
            if res == player:
                return player
    
    return other(player)

def winner_worst_play(visible, deck, player=1):
    if visible == [] or deck == []:
        return other(player)
    
    move_available = False
    for card_chosen in deck:
        for stack_chosen in visible:
            if stack_chosen[1] != card_chosen[1] or stack_chosen[0] > card_chosen[0]: # you cant put that card on top of the other one
                continue
            move_available = True
            new_visible = [card_chosen if card == stack_chosen else card for card in visible]
            new_deck = [card for card in deck if card != card_chosen]
            res = winner_worst_play(new_visible, new_deck, other(player))
            if res == other(player):
                return other(player)
    
    if not move_available:
        return other(player)
    
    return player

cards = list(itertools.product(range(n), range(s)))
count = 0
count2 = 0
table = []

for i in range(2**(len(cards))):
    b = bin(i)[2:].rjust(len(cards), "0")
    visible = []
    deck = []
    for j in range(len(cards)):
        if b[j] == "0":
            deck.append(cards[j])
        else:
            visible.append(cards[j])
            
            
    #winner = rec(visible, deck)
    higher = []
    for suit in range(s):
        add = []
        for card in visible:
            if card[1] != suit:
                continue
            count = 0
            for card2 in deck:
                if card2[1] != suit:
                    continue
                if card2[0] > card[0]:
                    count += 1
            add.append(count)
        if add:
            higher.append(tuple(add))
    
    higher.sort()
    higher = tuple(higher)
    higher = filter_zeros(higher)
    higher = base2(higher)
    
    w = rec3_2(higher)
    if w == -1:
        count2 += 1
        #table.append((higher, w))

# table.sort()
# print(tabulate(table))

print(count2)
print(time() - start, "s")