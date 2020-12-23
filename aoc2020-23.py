#!/usr/bin/python3

def partone():

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

    deck = [1,5,7,6,2,3,9,8,4]
    cur = deck[0]
    d = deck
    for t in range(1, 101):
        cur, d = playgame(cur, d)
    answer = ''.join([str(num) for num in result(d)])
    return(answer)


def parttwo(seed):

    def initiate(seed, top):
        ring = {}
        ring[top] = seed[0]
        i = 0
        while i < len(seed)-1:
            ring[seed[i]] = seed[i+1]
            i += 1
        ring[seed[-1]] = len(seed)+1
        return(ring)

    def after(ring, this):
        if this not in ring.keys():
            ring[this] = this+1
        return(ring[this])

    def place(ring, pos, hand):
        aft = after(ring, pos) #pekare efter instoppet
        ring[pos] = hand[0] #stoppa in handen efter position
        ring[hand[-1]] = aft #sista i handen ska peka efter instoppet
        return(ring)

    def move(ring, current):
        one = after(ring, current)
        two = after(ring, one)
        three = after(ring, two)
        hand = [one, two, three]
        ring[current] = after(ring, three)
        dest = current -1
        while dest in hand:
            dest -= 1
        if dest == 0:
            dest = max(ring.keys())

        ring = place(ring, dest, hand)
        next = after(ring, current)
        return(ring, next)

    top = 1000000
    time = 0
    current = seed[0]
    ring = initiate(seed, top)
    while time < 10000000:
        ring, current = move(ring, current)
        time += 1
    one = after(ring, 1)
    two = after(ring, one)
    return(one*two)

print('Advent of Code 2020, day 23 part 1')
print(partone())
print('Advent of Code 2020, day 23 part 2')
print(parttwo([1,5,7,6,2,3,9,8,4]))
#print(111057672960)
