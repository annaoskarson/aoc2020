#!/usr/bin/python3

with open('aoc2020-03-input.txt', 'r') as f:
  lines = f.read().split('\n')[:-1]

#lines = ['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#']

def partone(x, y):
    trees = 0
    for (i, l) in enumerate(lines):
        pos = (x*i)
        linenumber = (i*y)
        if linenumber > len(lines):
            return(trees)
        else:
            line = lines[linenumber]
            if pos >= len(line):
                newpos = pos % len(line)
                pos = newpos
            if line[pos] == '#':
                trees +=1
    return(trees)

def parttwo():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    number = 1
    for (x,y) in slopes:
        new = partone(x,y)
        number = number * new
    return(number)

print('Advent of Code 2020, day 3 part 1')
print(str(partone(3,1)) + ' is the number of trees.')
print('Advent of Code 2020, day 3 part 2')
print(str(parttwo()) + ' is the number.')
