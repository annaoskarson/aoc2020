#!/usr/bin/python3
with open('aoc2020-24-input.txt', 'r') as f:
    instructions = f.read().strip().split('\n')

#instructions = ['sesenwnenenewseeswwswswwnenewsewsw','neeenesenwnwwswnenewnwwsewnenwseswesw','seswneswswsenwwnwse','nwnwneseeswswnenewneswwnewseswneseene','swweswneswnenwsewnwneneseenw','eesenwseswswnenwswnwnwsewwnwsene','sewnenenenesenwsewnenwwwse','wenwwweseeeweswwwnwwe','wsweesenenewnwwnwsenewsenwwsesesenwne','neeswseenwwswnwswswnw','nenwswwsewswnenenewsenwsenwnesesenew','enewnwewneswsewnwswenweswnenwsenwsw','sweneswneswneneenwnewenewwneswswnese','swwesenesewenwneswnwwneseswwne','enesenwswwswneneswsenwnewswseenwsese','wnwnesenesenenwwnenwsewesewsesesew','nenewswnwewswnenesenwnesewesw','eneswnwswnwsenenwnwnwwseeswneewsenese','neswnwewnwnwseenwseesewsenwsweewe','wseweeenwnesenwwwswnew']

def move(start, instr):
    x,y = start
    i = 0
    while i < len(instr):
        if instr[i:].startswith('e'):
            x +=2
        elif instr[i:].startswith('w'):
            x -=2
        elif instr[i:].startswith('se'):
            y -=1
            x +=1
            i +=1
        elif instr[i:].startswith('sw'):
            y -=1
            x -=1
            i +=1
        elif instr[i:].startswith('ne'):
            y +=1
            x +=1
            i +=1
        elif instr[i:].startswith('nw'):
            y +=1
            x -=1
            i +=1
        else:
            print('wrong code')
        i += 1
    return(x,y)

def partone():
    black = set()
    for i in instructions:
        tile = move((0,0), i)
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)
    return(black)

def adjacent(x,y):
    return([(x-1,y+1),(x+1,y+1),(x+2,y),(x+1,y-1),(x-1,y-1),(x-2,y)])

def dayflip(b, size):
    [(xmin,ymin),(xmax,ymax)] = size
    towhite = set()
    toblack = set()
    for y in range(ymin, ymax+1):
        if y % 2 == 0:
            if xmin % 2 != 0:
                xmin -= 1
        else:
            if xmin % 2 == 0:
                xmin -= 1
        for x in range(xmin, xmax+1, 2):
            adj = adjacent(x,y)
            baround = len([tile for tile in adj if tile in b])
            if (x,y) not in b and baround == 2:
                toblack.add((x,y))
            elif (x,y) in b and (baround == 0 or baround > 2):
                towhite.add((x,y))
    b = b.union(toblack) - towhite
    return(b)

def size(flipped):
    return([(min(flipped, key=lambda x:x[0])[0]-2, min(flipped, key=lambda x:x[1])[1]-1), \
    (max(flipped, key=lambda x:x[0])[0]+2, max(flipped, key=lambda x:x[1])[1]+1)])

def parttwo():
    black = set(partone())
    for i in range(1,101):
        floorsize = size(black)
        black = dayflip(black, floorsize)
    return(len(black))

print('Advent of Code 2020, day 24 part 1')
print(len(partone()))
print('Advent of Code 2020, day 19 part 2')
print(parttwo())
