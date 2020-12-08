#!/usr/bin/python3
import copy

with open('aoc2020-08-input.txt', 'r') as f:
    textcode = f.read().strip().split('\n')

#textcode = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']

def makecode(text):
    code = []
    for line in text:
        code.append((line.split(' ')[0], int(line.split(' ')[1])))
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
        if i in been:
            loop = True
    return(accv, loop)

def partone():
    (answer, _) = runcode(code)
    return(answer)

def parttwo():
    testlist = [num for [num, (c, _)] in list(enumerate(code)) if c in ['jmp', 'nop']]
    for a in testlist:
        testcode = copy.deepcopy(code)
        (cmd, val) = code[a]
        testcode[a] = (next(item for item in ['jmp', 'nop'] if item not in cmd), val)
        (result, loop) = runcode(testcode)
        if not(loop):
            return(result)

code = makecode(textcode)
print('Advent of Code 2020, day 8 part 1')
print(partone())
print('Advent of Code 2020, day 8 part 2')
print(parttwo())
