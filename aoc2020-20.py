#!/usr/bin/python3
import math
with open('aoc2020-20-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')+['']

#print(lines[-2:])

puzzle = {}
start = 0
for i,l in enumerate(lines):
    if l == '':
        puzzle[tile] = lines[start:i]
    elif l[0] == 'T':
        tile = int(l.split(' ')[1][:-1])
        start = i+1

size = int(math.sqrt(len(puzzle)))

alla = []
kanter = {}
for bit in puzzle.keys():
    up = puzzle[bit][0]
    down = puzzle[bit][-1]
    left = ''.join([x[0] for x in puzzle[bit]])
    right = ''.join([x[-1] for x in puzzle[bit]])
    kanter[bit] = ([up, down, left, right], [up[::-1], down[::-1], left[::-1], right[::-1]])
    alla = alla + [up, up[::-1], down, down[::-1], left, left[::-1], right, right[::-1]]

def edges(bit):
    up = bit[0]
    down = bit[-1]
    left = ''.join([x[0] for x in bit])[::-1]
    right = ''.join([x[-1] for x in bit])
    return(up, right, down, left)

unique = []
def find_corners():
    global unique
    global alla
    unique = [x for x in alla if alla.count(x)==1]
    corners = []
    for bit in puzzle.keys():
        sides = [item for sublist in kanter[bit] for item in sublist]
        if len(set(sides) & set(unique)) == 4:
            corners.append(bit)
    return(corners)

def rotate(deg, bit):
    #pr(bit)
    if deg == 180:
        rbit = []
        for b in bit:
            rb = b[::-1]
            rbit.append(rb)
        bit = rbit[::-1]
    elif deg == 90:
        bit = [''.join(s) for s in zip(*bit)]
        bit = [s[::-1] for s in bit]
    elif deg == 270:
        bit = [''.join(s) for s in zip(*bit)]
        bit = [s[::-1] for s in bit]
        rbit = []
        for b in bit:
            rb = b[::-1]
            rbit.append(rb)
        bit = rbit[::-1]
    elif deg == 0:
        pass
    return(bit)

def mirror(bit):
    return(bit[::-1])

def pr(bit): #hjälpfunktion vid felsökning
    for row in bit:
        print(row)

def lay_puzzle():
    global size
    layed = {}
    used = []
    corners = find_corners()
    (up, right, down, left) = edges(puzzle[corners[0]])
    if (up in unique, right in unique, down in unique, left in unique) == (True, False, False, True):
        layed[1] = puzzle[corners[0]]
        used.append(corners[0])

    while len(layed) < size * size:
        if (len(layed) % size) != 0:
            (_, right, _, _) = edges(layed[len(layed)])
            for bit in puzzle.keys():
                if (right in edges(puzzle[bit]) or right[::-1] in edges(puzzle[bit])) and bit not in used:

                    thisbit = puzzle[bit]

                    (u,r,d,l) = edges(thisbit)
                    if right == u:
                        thisbit = mirror(rotate(270, thisbit))
                    elif right == u[::-1]:
                        thisbit = rotate(270, thisbit)
                    elif right == d:
                        thisbit = mirror(rotate(90, thisbit))
                    elif right == d[::-1]:
                        thisbit = mirror(rotate(90, thisbit))
                    elif right == r:
                        thisbit = mirror(rotate(180, thisbit))
                    elif right == r[::-1]:
                        thisbit = rotate(180, thisbit)
                    elif right == l:
                        thisbit = mirror(thisbit)
                    elif right == l[::-1]:
                        pass

                    layed[len(layed)+1] = thisbit
                    used.append(bit)
                    break
        else: #Om det är första i en rad.
            oldbitnum = len(layed) - (size-1)
            (_, _, down, _) = edges(layed[oldbitnum])
            for bit in puzzle.keys():
                if (down in edges(puzzle[bit]) or down[::-1] in edges(puzzle[bit])) and bit not in used:

                    thisbit = puzzle[bit]

                    (u,r,d,l) = edges(thisbit)
                    if down == u:
                        pass
                    elif down == u[::-1]:
                        thisbit = rotate(180, mirror(thisbit))
                    elif down == d:
                        thisbit = mirror(thisbit)
                    elif down == d[::-1]:
                        thisbit = rotate(180, thisbit)
                    elif down == r:
                        thisbit = rotate(270, thisbit)
                    elif down == r[::-1]:
                        thisbit = rotate(270, mirror(thisbit))
                    elif down == l:
                        thisbit = rotate(90, thisbit)
                    elif down == l[::-1]:
                        thisbit = rotate(90, mirror(thisbit))

                    layed[len(layed)+1] = thisbit
                    used.append(bit)
                    break
    return(layed)


def partone():
    corners = find_corners()
    return(corners[0]*corners[1]*corners[2]*corners[3])

def monster_present(x,y,karta):
    monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    compare = [karta[y][x:], karta[y+1][x:], karta[y+2][x:]]

    for i,row in enumerate(monster):
        for j,c in enumerate(row):
            if c == '#' and (compare[i][j] not in ['#', 'O']):
                return(False)
    return(True)

def paint_monster(x,y,karta):
    monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    for i,row in enumerate(monster):
        for j,c in enumerate(row):
            if c == '#':
                karta[y+i] = karta[y+i][:x+j] + 'O' + karta[y+i][x+j+1:]
    return(karta)

def mapsearch(themap):
    global size
    monsters = 0
    for y in range(0, len(themap)-2):
        for x in range(0, len(themap[0])-19):
            if monster_present(x,y,themap):
                monsters += 1
                themap = paint_monster(x,y,themap)
                monster_present(x,y,themap)
    return(themap)

def count_waves(themap):
    return(sum([row.count('#') for row in themap]))

def parttwo():
    image = lay_puzzle()

    for bit in image.keys():
        image[bit] = [row[1:-1] for row in image[bit]]
        image[bit] = image[bit][1:-1]

    themap = []
    for row in range(1, (size+1)):
        therow = image[(row-1)*size +1]
        for bit in range((row-1)*size+2, row*size+1):
            for i,str in enumerate(image[bit]):
                therow[i] += str
        themap.extend(therow)

    #Efter att ha tröskat igenom alla såg jag att det var map4 som var rätt ...
    #Men det går lika bra att tröska igenom alla, för det hittades inte fler monster.
    map1 = mapsearch(themap)
    map2 = mapsearch(rotate(90, map1))
    map3 = mapsearch(rotate(90, map2))
    map4 = mapsearch(rotate(90, map3))
    map5 = mapsearch(mirror(map4))
    map6 = mapsearch(rotate(90, map5))
    map7 = mapsearch(rotate(90, map6))
    map8 = mapsearch(rotate(90, map7))


    waves = count_waves(map8)
    # Om man vet hur det ska roteras så kan man göra såhär ...
    #waves = count_waves(mapsearch(rotate(270, themap)))
    return(waves)

print('Advent of Code 2020, day 20 part 1')
print(partone())
print('Advent of Code 2020, day 20 part 2')
print(parttwo())
