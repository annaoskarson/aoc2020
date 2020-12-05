#!/usr/bin/python3

with open('aoc2020-05-input.txt', 'r') as f:
    seats = [int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for line in f]

def missing(IDs):
    return(next(id + 1 for (i, id) in enumerate(IDs[:-1]) if id + 2 == IDs[i+1])) # Trying compact style

print('Advent of Code 2020, day 5 part 1')
print(max(seats))
print('Advent of Code 2020, day 5 part 2')
print(missing(sorted(seats)))
