#!/usr/bin/python3
import copy
with open('aoc2020-12-input.txt', 'r') as f:
    navigator = []
    for line in f:
        navigator.append(line.strip())

#navigator = ['F10', 'N3', 'F7', 'R90', 'F11']
#navigator = ['F10', 'R90', 'N10', 'L180', 'W20', 'R90', 'F10', 'E10']

def navigate(me, text):
    (x, y, v) = (me[0], me[1], me[2])
    (com, val) = (text[0], int(text[1:]))
    if com == 'N':
        y += val
    elif com == 'S':
        y -= val
    elif com == 'W':
        x -= val
    elif com == 'E':
        x += val
    elif com == 'R':
        v = (v + val) % 360
    elif com == 'L':
        v = (v + (360 - val)) % 360
    elif com == 'F':
        if v == 0:
            y += val
        elif v == 90:
            x += val
        elif v == 180:
            y -= val
        elif v == 270:
            x -= val
        else:
            print('vinkelfel')
    else:
        print('kommandofel')
    return([x, y, v])

def partone():
    me = [0, 0, 90]
    for command in navigator:
        me = navigate(me, command)
    return(abs(me[0]) + abs(me[1]))

def navigate2(me, wp, text):
    (x, y) = (me[0], me[1])
    (wx, wy) = (wp[0], wp[1])
    (com, val) = (text[0], int(text[1:]))
    if com == 'N':
        wy += val
    elif com == 'S':
        wy -= val
    elif com == 'W':
        wx -= val
    elif com == 'E':
        wx += val
    elif com in ['R', 'L']: #Rotate waypoint around me
        if (com == 'R' and val == 90) or (com == 'L' and val == 270):
            (wx, wy) = (wy, -wx)
        elif (com == 'R' and val == 270) or (com == 'L' and val == 90):
            (wx, wy) = (-wy, wx)
        elif val == 180:
            (wx, wy) = (-wx, -wy)
    elif com == 'F':
        x = val * wx + x
        y = val * wy + y
    else:
        print('kommandofel')
    return([x, y], [wx, wy])

def parttwo():
    me = [0, 0]
    wp = [10, 1]
    for command in navigator:
        (me, wp) = navigate2(me, wp, command)
    return(abs(me[0]) + abs(me[1]))

print('Advent of Code 2020, day 12 part 1')
print(partone())
print('Advent of Code 2020, day 12 part 2')
print(parttwo())
