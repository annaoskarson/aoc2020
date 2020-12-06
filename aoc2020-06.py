#!/usr/bin/python3
import re

with open('aoc2020-06-input.txt', 'r') as f:
    groups = f.read().strip().split('\n\n')

answers = []
for p in groups:
    answers.append(p.split('\n'))

#answers = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]

def partone(ans):
    count = 0
    for group in ans:
        grset = set(group[0])
        [grset.update(p) for p in group]
        count += len(grset)
    return(count)

def parttwo(ans):
    count = 0
    for group in ans:
        grset = set(group[0])
        for p in group:
            grset = grset & set(p)
        count += len(grset)
    return(count)

print('Advent of Code 2020, day 4 part 1')
print(partone(answers))
print('Advent of Code 2020, day 4 part 2')
print(parttwo(answers))
