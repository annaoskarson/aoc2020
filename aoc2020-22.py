#!/usr/bin/python3
import copy
import time

def deal():
    with open('aoc2020-22-input.txt', 'r') as f:
        lines = f.read().strip().split('\n')+['']
    p1 = []
    p2 = []
    for i,l in enumerate(lines):
        if l == '':
            if p == 'Player 1:':
                p1 = [int(x) for x in lines[start:i]]
            elif p == 'Player 2:':
                p2 = [int(x) for x in lines[start:i]]
        elif l[0] == 'P':
            p = l
            start = i+1
    return(p1, p2)

def playgame(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.extend([c1,c2])
        else:
            p2.extend([c2, c1])
    if len(p1) > len(p2):
        return(p1)
    else:
        return(p2)

def partone():
    p1, p2 = deal()
    return(score(playgame(p1, p2)))

def playgame2(p1, p2):
    allhands = set()
    while len(p1) > 0 and len(p2) > 0:
        if (score(p1), score(p2)) in allhands:
            winner = 1
            return(winner, p1, p2)
        allhands.add((score(p1), score(p2)))

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if c1 <= len(p1) and c2 <= len(p2): #Go into sub game
            # Preparing new hands for the sub game
            p1sub = copy.deepcopy(p1[:c1])
            p2sub = copy.deepcopy(p2[:c2])
            # Playing sub game to see who wins
            winner, _, _ = playgame2(p1sub, p2sub)
            #Subgame ended
        else:
            # If not subgame, play an ordinary game
            if c1 > c2:
                winner = 1
            else:
                winner = 2
        # Give cards to winner
        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return(winner, p1, p2)

def score(p):
    score = 0
    for i in range(1, len(p)+1):
        score += p[-i] * i
    return(score)

def parttwo():
    p1, p2 = deal()
    (winner, p1, p2) = playgame2(p1,p2)
    if winner == 1:
        return(score(p1))
    else:
        return(score(p2))

print('Advent of Code 2020, day 22 part 1')
print(partone())
print('Advent of Code 2020, day 22 part 2')
print(parttwo())
