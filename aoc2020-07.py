#!/usr/bin/python3
#import sys;i=sys.version_info;print("%d.%d"%(i.major,i.minor))
with open('aoc2020-07-input.txt', 'r') as f:
    text = f.read().strip().split('\n')
#text = ['light red bags contain 1 bright white bag, 2 muted yellow bags.','dark orange bags contain 3 bright white bags, 4 muted yellow bags.','bright white bags contain 1 shiny gold bag.','muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.','shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.','dark olive bags contain 3 faded blue bags, 4 dotted black bags.','vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.','faded blue bags contain no other bags.','dotted black bags contain no other bags.']

bagage = {}
for t in text:
    bag = ' '.join(t.split(' ')[:2])
    bagage[bag] = []
    bagsin = t.split(' ', 4)[-1].split(',')
    for i in bagsin:
        [nbr, bagin] = i.strip().split(' ', 1)
        bagin = ' '.join(bagin.split(' ')[:2])
        if nbr.isnumeric():
            nbr = int(nbr)
        elif nbr == 'no':
            nbr = 0
            bagin = ''
        for n in range(nbr):
            bagage[bag].append(bagin)

def printb():
    for b in bagage.keys():
        print(b, bagage[b])

#printb()
print(len(text), '=', len(bagage))

def inbag(q, bag):
    if bagage[bag] == []:
        return(False)
    elif q in set(bagage[bag]):
        return(True)
    else:
        for a in set(bagage[bag]):
            if q in set(bagage[a]):
                return(True)
            else:
                inbag(q, a)

question = 'shiny gold'
c = 0
vb = []
for b in bagage.keys():
    if inbag(question, b):
        vb.append(b)

#print('valid bags:', vb)
#print(len(vb), len(set(vb)))

print('Advent of Code 2020, day 4 part 1')
print(len(vb)) #30 was wrong
#print('Advent of Code 2020, day 4 part 2')
#print(parttwo(answers))
