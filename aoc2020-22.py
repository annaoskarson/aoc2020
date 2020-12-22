#!/usr/bin/python3

def deal():
    with open('aoc2020-22-input.txt', 'r') as f:
        lines = f.read().strip().split('\n')+['']
    p1 = []
    p2 = []
    for i,l in enumerate(lines):
        #print(l)
        if l == '':
            if p == 'Player 1:':
                p1 = [int(x) for x in lines[start:i]]
            elif p == 'Player 2:':
                p2 = [int(x) for x in lines[start:i]]
        elif l[0] == 'P':
            p = l
            start = i+1
    return(p1, p2)

def playcard(p1, p2):
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    elif c2 > c1:
        p2.append(c2)
        p2.append(c1)
    return(p1, p2)

def partone():
    p1, p2 = deal()

    while len(p1) > 0 and len(p2) > 0:
        p1, p2 = playcard(p1, p2)
    if len(p1) > len(p2):
        winner = p1
    else:
        winner = p2
    score = 0
    for i in range(1, len(winner)+1):
        score += winner[-i] * i
    return(score)

print('Advent of Code 2020, day 22 part 1')
print(partone())
#print('Advent of Code 2020, day 22 part 2')
#print(parttwo())
