#!/usr/bin/python3
with open('aoc2020-17-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

#lines = ['.#.','..#','###']

#print(lines)
world = set()
xrange = [0, len(lines[0])-1]
yrange = [0, len(lines)-1]
zrange = [0, 0]

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            world.add((x,y,0))

def naboer(x0,y0,z0):
    global world
    num = 0
    for x in range(x0-1, x0+2):
        for y in range(y0-1, y0+2):
            for z in range(z0-1, z0+2):
                if (x,y,z) in world and (x,y,z) != (x0,y0,z0):
                    num += 1
    return(num)

def deactivate(p):
    (x0,y0,z0) = p
    #print(x0, y0, z0, 'has nabos: ', naboer(x0,y0,z0))
    if naboer(x0,y0,z0) != 2 and naboer(x0,y0,z0) != 3:
        #print('deact')
        return(True)

def activate(p):
    (x0,y0,z0) = p
    if naboer(x0,y0,z0) == 3:
        return(True)

def partone():
    global world
    for i in range(1,7):
        deact = set()
        act = set()
        xrange[0] -= 1
        xrange[1] += 1
        yrange[0] -= 1
        yrange[1] += 1
        zrange[0] -= 1
        zrange[1] += 1
        for place in world: #check all the active places
            if deactivate(place):
                deact.add(place)
        for x in range(xrange[0], xrange[1]+1):
            for y in range(yrange[0], yrange[1]+1):
                for z in range(zrange[0], zrange[1]+1):
                    if ((x,y,z) not in world) and activate((x,y,z)):
                        act.add((x,y,z))
        world = (world - deact) | act


    return(len(world))




print('Advent of Code 2020, day 17 part 1')
print(partone())
#print('Advent of Code 2020, day 17 part 2')
#print(parttwo())
