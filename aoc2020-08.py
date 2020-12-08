#!/usr/bin/python3
import copy

def makecode(): # Makes code from text file.
    with open('aoc2020-08-input.txt', 'r') as f:
        code = []
        for line in f:
            code.append((line.strip().split(' ')[0], int(line.split(' ')[1])))
    return(code)

def runcode(c):
    (i, accv, step) = (0, 0, 0)
    been = []
    loop = False
    while not(loop) and i < len(c):
        been.append(i) # Save where we've been.
        (com, val) = c[i]
        if com == 'acc':
            accv += val
            step = 1
        elif com == 'jmp':
            step = val
        elif com == 'nop':
            step = 1

        i += step # Next position.
        if i in been: # If we have already been there.
            loop = True
    return(accv, loop)

def partone():
    (answer, _) = runcode(code)
    return(answer)

def parttwo():
    testlist = [num for [num, (c, _)] in list(enumerate(code)) if c in ['jmp', 'nop']] # Which positions to alter command at.
    for a in testlist:
        testcode = copy.deepcopy(code)
        (cmd, val) = code[a]
        testcode[a] = (next(item for item in ['jmp', 'nop'] if item not in cmd), val) # Change between jmp and nope for test.
        (result, loop) = runcode(testcode)
        if not(loop):
            return(result)

code = makecode()
print('Advent of Code 2020, day 8 part 1')
print(partone())
print('Advent of Code 2020, day 8 part 2')
print(parttwo())
