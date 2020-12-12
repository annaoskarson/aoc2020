#!/usr/bin/python3
import copy
with open('aoc2020-11-input.txt', 'r') as f:
    seats = []
    for line in f:
        seats.append(line.strip())

#seats = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']

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

def populate2(room):
    def checkline(x, y, compass):
        (dx, dy) = (0, 0)
        seat = ['L', '#']
        if 'n' in compass:
            dy = -1
        elif 's' in compass:
            dy = 1
        if 'e' in compass:
            dx = 1
        elif 'w' in compass:
            dx = -1
        x += dx
        y += dy
        while x >= 0 and x < len(room[0]) and y >= 0 and y < len(room):
            if room[y][x] in seat:
                return(room[y][x])
            x += dx
            y += dy
        return('-')

    def adjacent(x, y):
        adj = checkline(x, y, 'n') + checkline(x, y, 'ne') + checkline(x, y, 'e') + checkline(x, y, 'se') + checkline(x, y, 's') + checkline(x, y, 'sw') + checkline(x, y, 'w') + checkline(x, y, 'nw')
        return(adj)

    def cansit(x, y):
        if adjacent(x,y).count('#') == 0:
            return(True)

    def mustgo(x, y):
        if adjacent(x,y).count('#') >= 5:
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

def parttwo():
    states = []
    different = True
    newroom = populate2(seats)
    states.append(newroom)
    while different:
        newroom = populate2(newroom)
        states.append(newroom)
        if states[-1] == states[-2]:
            different = False
    return(occupied(states[-1]))


print('Advent of Code 2020, day 12 part 1')
print(partone())
print('Advent of Code 2020, day 12 part 2')
print(parttwo())
