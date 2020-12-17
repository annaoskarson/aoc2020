#!/usr/bin/python3
start = [0,8,15,2,12,1,4]

def partone():

    game = []
    game += start

    while len(game) < 2020:
        last = game[-1]
        if last not in game[:-1]:
            game.append(0)
        else:
            places = [i for i, x in enumerate(game) if x == last]
            game.append(places[-1] - places[-2])
    return(game[2019])

def parttwo():
    #start = [0,3,6]
    #start = [3,1,2]

    game = {}
    # Idea: Save each unique number together with where it was last seen.
    for (i, s) in enumerate(start[:-1], start=1):
        game[s] = i

    last = start[-1]
    length = len(start)
    while True:
        if last not in game.keys():
            next = 0
        else:
            seen = game[last] #When was the last number seen?
            next = length - seen #What will the next number be?
        game[last] = length #Write the last number to memory.
        length += 1
        if length == 30000000:
            return(next)
        last = next

print('Advent of Code 2020, day 15 part 1')
print(partone())
print('Advent of Code 2020, day 15 part 2')
print(parttwo())
