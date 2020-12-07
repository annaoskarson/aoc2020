#!/usr/bin/python3
import re

with open('aoc2020-04-input.txt', 'r') as f:
    lines = f.read().split('\n\n')

passlist = []
for line in lines:
    #print(re.split(r' +|\n+',line.strip()))
    passlist.append(re.split(r' +|\n+',line.strip()))

passports = []
for p in passlist:
    passport = {}
    for item in p:
        [key, value] = item.split(':')
        passport[key] = value
    passports.append(passport)

def basic_test(p):
    mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return(all(a in p.keys() for a in mandatory))

def adv_test(p):
    if basic_test(p):
        for item in p:
            if item == 'byr' and re.match(r'^(19[2-9][0-9]|200[0-2])$', p[item]) or \
            item == 'iyr' and re.match(r'^20(1[0-9]|20)$', p[item]) or \
            item == 'eyr' and re.match(r'^20(2[0-9]|30)$',p[item]) or \
            item == 'hgt' and re.match(r'^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$', p[item]) or \
            item == 'hcl' and re.match(r'^#[a-f\d]{6}$', p[item]) or \
            item == 'ecl' and re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', p[item]) or \
            item == 'pid' and re.match(r'^\d{9}$', p[item]) or \
            item == 'cid':
                pass
            else:
                return(False)
    else:
        return(False)
    return(True)

def partone(notchecked):
    v_list = []
    for p in notchecked:
        if basic_test(p):
            v_list.append(p)
    return(len(v_list))

def parttwo(notchecked):
    v2_list = []
    for p in notchecked:
        if adv_test(p):
            v2_list.append(p)
    return(len(v2_list))

print('Advent of Code 2020, day 4 part 1')
print(partone(passports))
print('Advent of Code 2020, day 4 part 2')
print(parttwo(passports))
