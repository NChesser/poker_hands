"""
Project Euler Problem 52
"""

with open("p054_poker.txt", "r") as f:
    poker = [[c for c in l.rstrip('\n').split()] for l in f]

card_values = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13,'A': 14}

def card_ranks(hand):
    return [card_values[r[0]] for r in hand]

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
    if full_house(ranks): return (7, full_house(ranks))
    if flush(ranks, suits): return (6, high(ranks))
    if straight(ranks): return (5, straight(ranks))
    if kinds(3, ranks): return (4, kinds(3, ranks))
    if two_pair(ranks): return (3, two_pair(ranks), high(ranks))
    if kinds(2, ranks): return (2, kinds(2, ranks), high(ranks))
    if high(ranks): return (1, high(ranks)) 

def winner(p1, p2):    
    #implement list of importance to loop thorugh
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
        print(p1)
        print(p2)
        total += winner(p1, p2)    
    return total

"""
Poker Hands
"""
def high(ranks):   
    return set([max(ranks)])

def kinds(number, ranks):   
    for c in ranks: 
        if ranks.count(c) == number:
            return set([c])

def two_pair(ranks):
    s = set(c for c in ranks if ranks.count(c) == 2)
    if len(s) == 2:
        return s
    return False

def full_house(ranks):
    s = set(c for c in ranks if ranks.count(c) == 2).union(set(c for c in ranks if ranks.count(c) == 3))
    if len(s) == 2:
        return s
    return False

def flush(ranks, suits):
    if set(c for c in suits if suits.count(c) == 4):
        return set([max(ranks)])
    return False

def straight(ranks):
    ranks = ranks.copy()
    s = set(c for c in ranks if max(ranks) - min(ranks) == len(ranks)-1)
    if len(s) == 5:
        return set([max(s)])
    if 14 in ranks:
        ranks.remove(14)
        ranks.append(1)
        s = set(c for c in ranks if max(ranks) - min(ranks) == len(ranks)-1)
        if len(s) == 5:
            return set([max(s)])
    return False

def straight_flush(ranks, suits):
    if len(set(suits)) != 1:
        return False
    return straight(ranks)
    
def royal_flush(ranks, suits):
    if max(ranks) != 14:
        return False
    return straight_flush(ranks, suits)

"""
Testing
"""
def tests():
    rf = "QD KD JD AD TD".split()
    sf = "2D 3D 4D 5D 6D".split()
    st = "2D 3C 4H 5D 6H".split()
    sta = "AD 2D 3H 4C 5D".split()
    fl = "6D 9D KD 7D 4C".split()
    fh = "6D 6C 6H 2H 2D".split()
    tp = "AD AC KD KC 2D".split()
    tp2 = "TD TC 3D 3C 2D".split()
    tk = "AD AC KD JD 3D".split()
    tk3 = "AD AC AD JD 3D".split()
    tk4 = "AD AC AS AH 3D".split()
    h = "AC 2D 3S 4D 9D".split()

    assert royal_flush(card_ranks(rf), card_suits(rf)) == set([14])
    assert straight_flush(card_ranks(sf), card_suits(sf)) == set([6])
    assert straight(card_ranks(st)) == set([6])
    assert straight(card_ranks(sta)) == set([5])
    
    assert flush(card_ranks(fl), card_suits(fl)) == set([13])
    assert full_house(card_ranks(fh)) == set([6,2])
    assert two_pair(card_ranks(tp)) == set([14,13])
    assert two_pair(card_ranks(tp2)) == set([10,3])
    
    assert kinds(2, card_ranks(tk)) == set([14])
    assert kinds(3, card_ranks(tk3)) == set([14])
    assert kinds(4, card_ranks(tk4)) == set([14])
    
    assert high(card_ranks(h)) == set([14])
    return "Tests Passed"

print(tests())
print(match())
    



