#!/usr/bin/python3

with open('aoc2020-09-input.txt', 'r') as f:
    numbers = []
    for line in f:
        numbers.append(int(line.strip()))

#numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

def partone():
    pre = 25
    for (i, n) in enumerate(numbers[:]):
        if i < pre:
            pass
        else:
            item = n
            check = numbers[i-pre:i]
            try:
                if next(True for (i, one) in enumerate(check) for two in check[i:] if one+two == item):
                    pass
            except StopIteration:
                return(n)

print('Advent of Code 2020, day 8 part 1')
print(partone())
print('Advent of Code 2020, day 8 part 2')
#print(parttwo())
