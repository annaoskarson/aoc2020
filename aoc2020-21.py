#!/usr/bin/python3
import re
with open('aoc2020-21-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


foods = []
for line in lines:
    contents = line.split('(')[0].split(' ')[:-1] #remove an empty string at the end
    allergenes = line.split('(')[1].replace('contains ', '').replace(')', '').replace(' ', '').split(',')
    foods.append((contents, allergenes))

all_allergenes = set([a for (_,sublist) in foods for a in sublist])


translation = {}

def partone():
    global translation
    for alg in all_allergenes:
        check = [c for (c, a) in foods if alg in a]
        elements_in_all = list(set.intersection(*map(set, check)))
        translation[alg] = elements_in_all

    done = False
    while not done:
        for alg in translation.keys():
            if len(translation[alg]) == 1:
                for a in translation.keys():
                    if a != alg:
                        translation[a] = list(set(translation[a]) - set(translation[alg]))
        if all(len(a) == 1 for a in translation.values()):
            done = True

    allergenes_food = [item for x in translation.keys() for item in translation[x]]

    result = 0
    for (f,a) in foods:
        allers = set(allergenes_food)
        result += len([item for item in f if item not in allers])
    return(result)

def parttwo():
    result = []
    for key, value in sorted(translation.items()):
        result += value
    return(','.join(result))


print('Advent of Code 2020, day 21 part 1')
print(partone())
print('Advent of Code 2020, day 21 part 2')
print(parttwo())
