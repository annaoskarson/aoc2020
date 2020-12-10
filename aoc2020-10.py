#!/usr/bin/python3

with open('aoc2020-10-input.txt', 'r') as f:
    adapters = []
    for line in f:
        adapters.append(int(line.strip()))

#adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
list.sort(adapters)

def partone():
    out = 0
    ones = 0
    threes = 0
    for a in adapters:
        if a == out + 1:
            ones += 1
        elif a == out + 3:
            threes += 1
        out += (a-out)
    threes += 1
    return(ones * threes)


print('Advent of Code 2020, day 10 part 1')
print(partone())
print('Advent of Code 2020, day 10 part 2')
#print(parttwo())
