#!/usr/bin/python3

with open('aoc2020-10-input.txt', 'r') as f:
    adapters = []
    for line in f:
        adapters.append(int(line.strip()))

#adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
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

def parttwo():
    global adapters
    result = 1
    adapters = [0] + adapters + [adapters[-1]+3]
    i = 1
    one = 0
    while i in range(len(adapters)):
        if adapters[i] == adapters[i-1] + 1:
            one += 1
        else:
            if one == 2:
                result *= 2
            elif one == 3:
                result *= 4
            elif one == 4:
                result *= 7
            one = 0
        i += 1
    return(result)

# 2 : 2
# 3 : 4
# 4 : 7

print('Advent of Code 2020, day 10 part 1')
print(partone())
print('Advent of Code 2020, day 10 part 2')
print(parttwo())
