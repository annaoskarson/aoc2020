#!/usr/bin/python3
import regex
with open('aoc2020-19-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

#lines = ['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', '5: "b"', '','ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
#lines = ['0: 1 2', '1: "a"', '2: 1 3 | 3 1', '3: "b"', '', 'aab', 'aba', 'bbb']
#lines = ['0: 1 2', '1: "a"', '2: "b"', '', 'ab', 'a', 'ba']

rules = {}
for i, line in enumerate(lines):
    if line.isalpha():
        messages = lines[i:]
        break
    elif ':' in line:
        rulenbr, rule = line.split(':')
        rule = rule.strip().replace('"', '')
        if not regex.match(r'(a|b)', rule):
            rule = rule.strip().replace('"', '').split('|')
            for i in range(len(rule)):
                rule[i] = [x for x in rule[i].strip().split(' ')]
        rules[rulenbr] = rule

def pattern(num):
    global part
    ll = rules[num]

    if num == '8' and part == 2:
        #rules['8'] = [['42'], ['42', '8']]
        return('(' + pattern('42') + ')+' )
    elif num == '11' and part == 2: #(apa)(?R)?(bepa
        #rules['11'] = [['42', '31'], ['42', '11', '31']]
        #return('(' + pattern('42') + '(?-1)?' + pattern('31') +')' )
        #return('((' + pattern('42') + ')(?R)?(' + pattern('31') +'))' )
        # Fick aldrig ordning på det, oklart.
        #return('(' + pattern('42') + pattern('31') + '|' + \
        #pattern('42') + pattern('42') + pattern('31') + pattern('31') + '|' + \
        #pattern('42') + pattern('42') + pattern('42') + pattern('31') + pattern('31') + pattern('31') + '|' + \
        #pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + '|' + \
        #pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + '|' +
        #pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('42') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + pattern('31') + ')' )

        return('(' + pattern('42') + pattern('31') + '|' + \
        '(' + pattern('42') +'){2}(' + pattern('31') + '){2}' + '|' + \
        '(' + pattern('42') +'){3}(' + pattern('31') + '){3}' + '|' + \
        '(' + pattern('42') +'){4}(' + pattern('31') + '){4}' + '|' + \
        '(' + pattern('42') +'){5}(' + pattern('31') + '){5}' + '|' + \
        '(' + pattern('42') +'){6}(' + pattern('31') + '){6}' + ')' )


    if len(ll) == 1:
        l = ll[0]
        if len(l) == 1:
            if l[0].isalpha():
                return(l[0])
            else:
                return(pattern(l[0]))
        else:
            return(''.join([pattern(x) for x in l]))
    elif len(ll) == 2:
        return('(' + ''.join([pattern(x) for x in ll[0]] + ['|'] + [pattern(x) for x in ll[1]]) + ')')


def partone():
    global part
    part = 1
    result = 0
    PAT = pattern('0')
    for m in messages:
        if regex.match(rf'\b(?=\w){PAT}\b(?!\w)', m, regex.IGNORECASE):
            result += 1
    return(result)

def parttwo():
    global part
    part = 2
    result = 0

    PAT = pattern('0')
    for m in messages:
        if regex.match(rf'\b(?=\w){PAT}\b(?!\w)', m, regex.IGNORECASE):
            result += 1
            #print(m)
    return(result)
    #8: 42 | 42 8
    #11: 42 31 | 42 11 31

print('Advent of Code 2020, day 19 part 1')
print(partone())
print('Advent of Code 2020, day 19 part 2')
print(parttwo())
