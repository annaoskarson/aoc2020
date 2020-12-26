#!/usr/bin/python3
import re
with open('aoc2020-18-input.txt', 'r') as f:
    homework = f.read().strip().split('\n')

#homework = ['2 * 3 + (4 * 5)','5 + (8 * 3 + 9 + 3 * 4 * 3)','5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))','((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
#homework = ['1 + 2 * 3 + 4 * 5 + 6']
#homework = ['1 + (2 * 3) + (4 * (5 + 6))']
#homework = ['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']
#homework = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']

def calculate(expr):
    i = 1
    result = expr[0]
    while i < len(expr):
        if expr[i] == '*':
            i += 1
            result = result * expr[i]
            i += 1
        elif expr[i] == '+':
            i += 1
            result = result + expr[i]
            i += 1
    return(result)

def solve(row):
    up = []
    i = 0
    row = '(' + row + ')'
    expr = []
    while i < len(row):
        if re.match(r'^[0-9]', row[i:]):
            expr.append(int(row[i]))
        elif re.match(r'^\*', row[i:]):
            expr.append(row[i])
        elif re.match(r'^\+', row[i:]):
            expr.append(row[i])
        elif re.match(r'^\(', row[i:]):
            up.append(len(expr))
        elif re.match(r'^\)', row[i:]):
            start = up.pop()
            result = calculate(expr[start:])
            expr = expr[:start] + [result]
        i += 1
    return(calculate(expr))

def partone():
    result = []
    for hw in homework:
        hw = hw.replace(' ', '')
        result.append((solve(hw)))
    return(sum(result))

def calculate2(expr):
    i = 1

    while i < len(expr):
        if expr[i] == '+':
            expr = expr[:i-1] + [expr[i-1] + expr[i+1]] + expr[i+2:]
        elif expr[i] == '*':
            i += 2

    i = 1
    result = expr[0]
    while i < len(expr):
        if expr[i] == '*':
            result = result * expr[i+1]
            i += 2

    return(result)

def solve2(row):
    up = []
    i = 0
    row = '(' + row + ')'
    expr = []
    while i < len(row):
        if re.match(r'^[0-9]', row[i:]):
            expr.append(int(row[i]))
        elif re.match(r'^\*', row[i:]):
            expr.append(row[i])
        elif re.match(r'^\+', row[i:]):
            expr.append(row[i])
        elif re.match(r'^\(', row[i:]):
            up.append(len(expr))
        elif re.match(r'^\)', row[i:]):
            start = up.pop()
            result = calculate2(expr[start:])
            expr = expr[:start] + [result]
        i += 1
    return(calculate2(expr))

def parttwo():
    result = []
    for hw in homework:
        hw = hw.replace(' ', '')
        result.append((solve2(hw)))
    return(sum(result))

print('Advent of Code 2020, day 18 part 1')
print(partone()) # too low
print('Advent of Code 2020, day 18 part 2')
print(parttwo())
