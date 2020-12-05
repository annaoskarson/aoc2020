#!/usr/bin/python3
import re

with open('aoc2020-04-input.txt', 'r') as f:
    lines = f.read().split('\n\n')

passports = []
for line in lines:
    passport = re.split(r' +|\n+',line.strip())
    passports = passports + [passport]

valid = [False] * 7
checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def partone(passports):
    global valid, checks
    vpassports = []
    for p in passports:
        for post in p:
            try:
                valid[checks.index(post[:3])] = True
            except ValueError:
                pass
        if all(valid):
            vpassports = vpassports + [p]
        valid = [False] * 7
    return(vpassports)

def test(field, value):
    global valid
    if field == 'byr' and len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
        valid[checks.index(field)] = True
    elif field == 'iyr' and len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
        valid[checks.index(field)] = True
    elif field == 'eyr' and len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
        valid[checks.index(field)] = True
    elif field == 'hgt' and ((value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193) or ((value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76))):
        valid[checks.index(field)] = True
    elif field =='hcl' and re.match(r'[a-f\d]{6}', value[1:]):
        valid[checks.index(field)] = True
    elif field == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid[checks.index(field)] = True
    elif field == 'pid' and re.match(r'^\d{9}$', value):
        valid[checks.index(field)] = True

def parttwo(vpassports):
    global valid
    wpassports = []
    for p in vpassports:
        #print('p: ', p)
        for post in p:
            [field,value] = post.split(':')
            test(field,value)
        if all(valid):
            #print(valid, p)
            wpassports = wpassports + [p]
        else:
            pass
            #print(valid, p)
        valid = [False] * 7
    return(wpassports)

print('Advent of Code 2020, day 4 part 1')
print(len(partone(passports)))
print('Advent of Code 2020, day 4 part 2')
print(len(parttwo(partone(passports))))
