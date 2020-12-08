#!/usr/bin/python3
import copy

with open('aoc2020-08-input.txt', 'r') as f:
    code = f.read().strip().split('\n')

#code = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']

def runcode(code):
    i = 0
    been = []
    finish = False
    accv = 0
    while not(finish) and i < len(code):
        (com, val) = (code[i].split(' ')[0], int(code[i].split(' ')[1]))
        been.append(i)
        if com == 'acc':
            accv += val
            i += 1
        elif com == 'jmp':
            i += val
        elif com == 'nop':
            i += 1

        if i in been:
            finish = True
    if not(finish):
        print('here comes answer to part 2:')
    return(accv)

def partone():
    return(runcode(code))

def parttwo():
    testlist = list(enumerate(code))
    for (a, c) in testlist:
        testcode = copy.deepcopy(code)
        (com, val) = (c.split(' ')[0], int(c.split(' ')[1]))
        if com in ['jmp', 'nop']:
            if com == 'jmp':
                testcode[a] = c.replace('jmp', 'nop')
            elif com == 'nop':
                testcode[a] = c.replace('nop', 'jmp')
            result = runcode(testcode)
            print(result)
    #print(testlist)

print('Advent of Code 2020, day 8 part 1')
print(partone())
print('Advent of Code 2020, day 8 part 2')
print(parttwo())
