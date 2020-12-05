#!/usr/bin/python3

with open('aoc2020-05-input.txt', 'r') as f:
    seats = f.read().split('\n')[:-1]

#Test data
#seats = ['BFFFBBFRRR','FFFBBBFRRR', 'BBFFBBFRLL']

IDs = []
for s in seats:
    row = int(s[:7].replace('F', '0').replace('B', '1'), base=2)
    col = int(s[-3:].replace('L', '0').replace('R', '1'), base=2)
    IDs = IDs + [row*8+col]

IDs.sort()

def missing(IDs):
    for (i , id) in enumerate(IDs[:-1]):
        if (id + 2) == IDs[i+1]:
            return(id+1)

print('Advent of Code 2020, day 4 part 1')
print(max(IDs))
print('Advent of Code 2020, day 4 part 2')
print(missing(IDs))
