#!/usr/bin/python3
import re
with open('aoc2020-20-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')+['']

#print(lines[-2:])

puzzle = {}
start = 0
for i,l in enumerate(lines):
    if l == '':
        puzzle[tile] = lines[start:i]
    elif l[0] == 'T':
        tile = l.split(' ')[1][:-1]
        start = i+1

alla = []
kanter = {}
for bit in puzzle.keys():
    up = puzzle[bit][0]
    down = puzzle[bit][-1]
    left = ''.join([x[0] for x in puzzle[bit]])
    right = ''.join([x[-1] for x in puzzle[bit]])
    kanter[bit] = ([up, down, left, right], [up[::-1], down[::-1], left[::-1], right[::-1]])
    alla = alla + [up, up[::-1], down, down[::-1], left, left[::-1], right, right[::-1]]

def find_corners():
    global alla
    unique = [x for x in alla if alla.count(x)==1]
    corners = []
    for bit in puzzle.keys():
        sides = [item for sublist in kanter[bit] for item in sublist]
        if len(set(sides) & set(unique)) == 4:
            corners.append(int(bit))
    return(corners)

def partone():
    corners = find_corners()
    return(corners[0]*corners[1]*corners[2]*corners[3])

print('Advent of Code 2020, day 20 part 1')
print(partone())
#print('Advent of Code 2020, day 20 part 2')
#print(parttwo())
