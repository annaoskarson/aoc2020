#!/usr/bin/python3

with open('aoc2020-01-input.txt', 'r') as f:
  lines = f.read().split('\n')[:-1]

def partone():
    print('Advent of Code 2020, day 1 part 1')
    for (i,a) in enumerate(lines):
        for b in lines[i:]:
            if int(a)+int(b) == 2020:
                print(int(a)*int(b))
                return

def parttwo():
    print('Advent of Code 2020, day 1 part 2')
    for (i,a) in enumerate(lines):
        for (j,b) in enumerate(lines[i:]):
            for c in lines[j:]:
                if int(a) + int(b) + int(c) == 2020:
                    print(int(a)*int(b)*int(c))
                    return
partone()
parttwo()
