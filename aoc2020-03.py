#!/usr/bin/python3

with open('aoc2020-03-input.txt', 'r') as f:
  lines = f.read().split('\n')[:-1]

# Test input.
#lines = ['..##.......','#...#...#..','.#....#..#.','..#.#...#.#','.#...##..#.','..#.##.....','.#.#.#....#','.#........#','#.##...#...','#...##....#','.#..#...#.#']

def partone(x, y):
    trees = 0
    i = 0
    while (i*y) < len(lines):
        line = lines[i*y]
        xpos = (i*x) % len(line)
        if line[xpos] == '#':
            trees +=1
        i += 1
    return(trees)

def parttwo():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    number = 1
    for (x,y) in slopes:
        number = number * partone(x,y)
    return(number)

print('Advent of Code 2020, day 3 part 1')
print(str(partone(3,1)) + ' is the number of trees.')
print('Advent of Code 2020, day 3 part 2')
print(str(parttwo()) + ' is the number.')
