#!/usr/bin/python3
import copy
with open('aoc2020-11-input.txt', 'r') as f:
    seats = []
    for line in f:
        seats.append(line.strip())

#seats = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
#print(seats)

#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#Otherwise, the seat's state does not change.
#Floor (.) never changes; seats don't move, and nobody sits on the floor.

def populate(room):
    def adjacent(x, y):
        adj = ''
        if x-1 >= 0:
            adj += room[y][x-1]
            if y-1 >= 0:
                adj += room[y-1][x-1]
            if y+1 < len(room):
                adj += room[y+1][x-1]
        if y-1 >= 0:
            adj += room[y-1][x]
        if x+1 < len(room[y]):
            adj += room[y][x+1]
            if y-1 >= 0:
                adj += room[y-1][x+1]
            if y+1 < len(room):
                adj += room[y+1][x+1]
        if y+1 < len(room):
            adj += room[y+1][x]
        return(adj)

    def cansit(x, y):
        if adjacent(x,y).count('#') == 0:
            return(True)

    def mustgo(x, y):
        if adjacent(x,y).count('#') >= 4:
            return(True)

    newroom = copy.deepcopy(room)
    for (y, row) in enumerate(room):
        for (x, s) in enumerate(row):
            if s == 'L' and cansit(x, y):
                newroom[y] = newroom[y][:x] + '#' + newroom[y][x+1:]
            elif s == '#' and mustgo(x, y):
                newroom[y] = newroom[y][:x] + 'L' + newroom[y][x+1:]
            else:
                pass
    return(newroom)

def occupied(room):
    occ = 0
    for row in room:
        occ += row.count('#')
    return(occ)

def partone():
    states = []
    different = True
    newroom = populate(seats)
    states.append(newroom)
    while different:
        newroom = populate(newroom)
        states.append(newroom)
        if states[-1] == states[-2]:
            different = False
    return(occupied(states[-1]))

print('Advent of Code 2020, day 12 part 1')
print(partone())
#print('Advent of Code 2020, day 12 part 2')
#print(parttwo())
