#!/usr/bin/python3
with open('aoc2020-25-input.txt', 'r') as f:
    [doorpub, cardpub] = map(int, f.read().strip().split('\n'))
# Test data
#cardpub = 5764801
#doorpub = 17807724

def partone():
    result = 1
    encrypted = 1
    while result != cardpub:
        result = (result * 7) % 20201227
        encrypted = (encrypted * doorpub) % 20201227
    return(encrypted)

print('Advent of Code 2020, day 25 part 1')
print(partone())
