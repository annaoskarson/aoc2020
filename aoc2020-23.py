#!/usr/bin/python3

def destno(d, cur, thr):
    if cur == min(d):
        dest = max(d)
    else:
        dest = cur-1
    while dest in thr:
        if dest == min(d):
            dest = max(d)
        else:
            dest -=1
    return(dest)

def playgame(current, deck):
    rounddeck = deck + deck
    three = rounddeck[deck.index(current)+1: deck.index(current)+4]
    dest = destno(deck, current, three)
    deck = [c for c in deck if c not in three]
    deck = deck[:deck.index(dest)+1] + three + deck[deck.index(dest)+1:]

    if current == deck[-1]:
        newcur = deck[0]
    else:
        newcur = deck[deck.index(current)+1]
    return(newcur, deck)

def result(d):
    doubledeck = d + d
    return(doubledeck[doubledeck.index(1)+1 : doubledeck.index(1)+9])

def partone():
    deck = [1,5,7,6,2,3,9,8,4]
    cur = deck[0]
    d = deck
    for t in range(1, 101):
        cur, d = playgame(cur, d)
    answer = ''.join([str(num) for num in result(d)])
    return(answer)

print('Advent of Code 2020, day 23 part 1')
print(partone())
#print('Advent of Code 2020, day 23 part 2')
#print(parttwo())
