#!/usr/bin/python3

with open('aoc2020-04-input.txt', 'r') as f:
    lines = f.read().split('\n')

listan = []

for l in lines:
    a = l.split(' ')
    listan = listan + a

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
valid = 0
i = 0
while i < len(listan):
    if listan[i] == '':
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid +=1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
    else:
        pre = listan[i].split(':')[0]
        if pre == 'byr':
            byr = True
        if pre == 'iyr':
            iyr = True
        if pre == 'eyr':
            eyr = True
        if pre == 'hgt':
            hgt = True
        if pre == 'hcl':
            hcl = True
        if pre == 'ecl':
            ecl = True
        if pre == 'pid':
            pid = True
    #print(byr, iyr, eyr, hgt, hcl, ecl, pid)
    i += 1

print(valid)
print('part 2')

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
valid = 0
i = 0
while i < len(listan):
    if listan[i] == '':
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid +=1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
    else:
        [pre, post] = listan[i].split(':')
        #print(pre)
        #print(post)
        if pre == 'byr':
            if len(post) == 4 and int(post) >= 1920 and int(post) <= 2002:
                byr = True
        if pre == 'iyr':
            if len(post) == 4 and int(post) >= 2010 and int(post) <= 2020:
                iyr = True
        if pre == 'eyr':
            if len(post) == 4 and int(post) >= 2020 and int(post) <= 2030:
                eyr = True
        if pre == 'hgt':
            if (post[-2:] == 'cm' and int(post[:-2]) >= 150 and int(post[:-2]) <= 193) or (post[-2:] == 'in' and int(post[:-2]) >= 59 and int(post[:-2]) <= 76):
                hgt = True
        if pre == 'hcl':
            if post[0] == '#' and len(post) == 7 and (post[1:].isnumeric() or s in ['a', 'b', 'c', 'd', 'e', 'f'] for s in post[1:]):
                hcl = True
        if pre == 'ecl':
            if post in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                ecl = True
        if pre == 'pid':
            if len(post) == 9 and post.isnumeric():
                pid = True
    #print(byr, iyr, eyr, hgt, hcl, ecl, pid)
    i += 1
print(valid)
print('Advent of Code 2020, day 4 part 1')
#print(str(partone(3,1)) + ' is the number of trees.')
print('Advent of Code 2020, day 4 part 2')
#print(str(parttwo()) + ' is the number.')
