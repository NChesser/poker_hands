"""
Project Euler Problem 52
"""
with open("p054_poker.txt", "r") as f:
    poker = [[c for c in l.rstrip('\n').split()] for l in f]

card_values = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}

def card_ranks(hand):
    return sorted([card_values[r[0]] for r in hand], reverse=True)

def card_suits(hand):
    return [s[1] for s in hand]

"""
Getting Hand Values
"""

def hand_value(hand):
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    if royal_flush(ranks, suits): return (10, high(ranks))
    if straight_flush(ranks, suits): return (9, high(ranks))
    if kinds(4, ranks): return (8, kinds(4, ranks))
    if full_house(ranks): return (7, kinds(3, ranks), kinds(2, ranks))
    if flush(suits): return (6, high(ranks))
    if straight(ranks): return (5, high(ranks))
    if kinds(3, ranks): return (4, kinds(3, ranks), high(ranks))
    if two_pair(ranks): return (3, kinds(2, ranks), kinds(2, ranks), high(ranks))
    if kinds(2, ranks): return (2, kinds(2, ranks), high(ranks))
    if high(ranks): return (1, high(ranks))

"""
Determine the winner of a hand
"""

def winner(p1, p2):    
    for h1, h2 in zip(p1, p2):
        if h1 > h2:
            return 1
        elif h2 > h1:
            return 0
    else:
        return 0

def match():
    total = 0
    for i, p in enumerate(poker):
        p1 = hand_value(poker[i][:5])
        p2 = hand_value(poker[i][5:])
        total += winner(p1, p2)    
    return total

"""
Poker Hands
"""
def high(ranks):   
    return max(ranks)

def kinds(number, ranks):   
    for c in ranks: 
        if ranks.count(c) == number:
            ranks.reverse()
            return c

def two_pair(ranks):
    s = set(c for c in ranks if ranks.count(c) == 2)
    if len(s) == 2:
        return True
    return False

def full_house(ranks):
    if not set(c for c in ranks if ranks.count(c) == 3):
        return False    
    if not set(c for c in ranks if ranks.count(c) == 2):
        return False
    return True

def flush(suits):
    return len(set(suits)) == 1

def straight(ranks):    
    if len(set(c for c in ranks if max(ranks) - min(ranks) == len(ranks)-1)) == 5:
        return True
    ranks = ranks.copy()
    if 14 in ranks:
        ranks.remove(14)
        ranks.append(1)
        if len(set(c for c in ranks if max(ranks) - min(ranks) == len(ranks)-1)) == 5:
            return True
    return False

def straight_flush(ranks, suits):
    if not flush(suits):
        return False
    return straight(ranks)
    
def royal_flush(ranks, suits):
    if max(ranks) != 14:
        return False
    return straight_flush(ranks, suits)

print("Player 1 Won " + str(match()) + " Hands")
    



