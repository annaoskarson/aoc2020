#!/usr/bin/python3

with open('aoc2020-09-input.txt', 'r') as f:
    numbers = []
    for line in f:
        numbers.append(int(line.strip()))

#numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

def partone():
    pre = 25
    for i in range(pre, len(numbers)):
        n = numbers[i]
        check = numbers[i-pre:i]
        if next((False for (i, one) in enumerate(check) for two in check[i:] if one+two == n), True):
            return(n)

def parttwo():
    n = partone()
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if sum(numbers[i:j]) == n:
                return(max(numbers[i:j]) + min(numbers[i:j]))

print('Advent of Code 2020, day 9 part 1')
print(partone())
print('Advent of Code 2020, day 9 part 2')
print(parttwo())
