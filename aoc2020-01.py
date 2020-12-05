#!/usr/bin/python3

with open('aoc2020-01-input.txt', 'r') as f:
  lines = f.read().split('\n')[:-1]

def partone():
    for (i,a) in enumerate(lines):
        for b in lines[i:]:
            if int(a)+int(b) == 2020:
                return(int(a)*int(b))

def parttwo():
    for (i,a) in enumerate(lines):
        for (j,b) in enumerate(lines[i:]):
            for c in lines[j:]:
                if int(a) + int(b) + int(c) == 2020:
                    return(int(a)*int(b)*int(c))

def partone2(): #Take 2, with list comprehension.
    return[int(a)*int(b) for (i,a) in enumerate(lines) for b in lines[i:] if int(a)+int(b) == 2020]

def parttwo2(): #List comprehension, takes ages to run ...
    return([int(a)*int(b)*int(c) for (i,a) in enumerate(lines) for (j,b) in enumerate(lines[i:]) for c in lines[j:] if sum([int(a), int(b), int(c)]) == 2020][0])

print('Advent of Code 2020, day 1 part 1')
print(partone())
print(partone2())
print('Advent of Code 2020, day 1 part 2')
print(parttwo())
print(parttwo2())
