#!/usr/bin/python3
import re

with open('aoc2020-04-input.txt', 'r') as f:
    lines = f.read().split('\n\n')

passports = []
for line in lines:
    passports.append(re.split(r' +|\n+',line.strip()))

valid = [False] * 7
checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
vpassports = []

def partone(passports):
    global valid, checks, vpassports
    for p in passports:
        for post in p:
            if re.match(r'^(byr|iyr|eyr|hgt|hcl|ecl|pid):', post):
                valid[checks.index(post[:3])] = True
        if all(valid):
            vpassports.append(p)
        valid = [False] * 7
    return(vpassports)

def test(p):
    global checks
    global valid
    if (re.match(r'^byr:(19[2-9][0-9]|200[0-2])$', p) or \
    re.match(r'^iyr:20(1[0-9]|20)$', p) or \
    re.match(r'^eyr:20(2[0-9]|30)$',p) or \
    re.match(r'^hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$', p) or \
    re.match(r'^hcl:#[a-f\d]{6}$', p) or \
    re.match(r'^ecl:(amb|blu|brn|gry|grn|hzl|oth)$', p) or \
    re.match(r'^pid:\d{9}$', p)):
        valid[checks.index(p[:3])] = True

def parttwo(passports):
    global valid
    vpassports = []
    for p in passports:
        for post in p:
            test(post)
        if all(valid):
            vpassports.append(p)
        valid = [False] * 7
    return(vpassports)

print('Advent of Code 2020, day 4 part 1')
print(len(partone(passports)))
print('Advent of Code 2020, day 4 part 2')
print(len(parttwo(vpassports)))
