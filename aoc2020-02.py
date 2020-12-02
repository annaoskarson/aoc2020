#!/usr/bin/python3

with open('aoc2020-02-input.txt', 'r') as f:
  lines = f.read().split('\n')[:-1]

#print(len(lines))

def partone():
    print('Advent of Code 2020, day 2 part 1')
    valid = []
    for l in lines:
        low = l.split(' ')[0].split('-')[0]
        high = l.split(' ')[0].split('-')[1]
        char = l.split(' ')[1][:-1]
        word = l.split(' ')[2]
        number = word.count(char)
        if number <= int(high) and number >= int(low):
            valid = valid + [word]
    print(str(len(valid)) + ' correct passwords.')


def parttwo():
    print('Advent of Code 2020, day 2 part 2')
    valid = []
    for l in lines:
        one = l.split(' ')[0].split('-')[0]
        two = l.split(' ')[0].split('-')[1]
        char = l.split(' ')[1][:-1]
        word = l.split(' ')[2]
        if (word[int(one)-1] == char) != (word[int(two)-1] == char):
            valid = valid + [word]
    print(str(len(valid)) + ' correct passwords.')


partone()
parttwo()
