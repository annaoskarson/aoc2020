#!/usr/bin/python3
with open('aoc2020-07-input.txt', 'r') as f:
    text = f.read().strip().split('\n')
#text = ['light red bags contain 1 bright white bag, 2 muted yellow bags.','dark orange bags contain 3 bright white bags, 4 muted yellow bags.','bright white bags contain 1 shiny gold bag.','muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.','shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.','dark olive bags contain 3 faded blue bags, 4 dotted black bags.','vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.','faded blue bags contain no other bags.','dotted black bags contain no other bags.']

bagage = {}
for t in text:
    bag = ' '.join(t.split(' ')[:2])
    bagage[bag] = []
    bagsin = t.replace('.', '').split(' ', 4)[-1].split(',')
    for i in bagsin:
        (nbr, bagin) = (int(i.strip().split(' ')[0].replace('no', '0')), ' '.join(i.strip().split(' ')[1:3]))
        for n in range(nbr):
            bagage[bag].append(bagin)

def inbag(q, bag):
    for a in set(bagage[bag]):
        if a == q:
            return(True)
        if inbag(q, a):
            return(True)
    return(False)

def partone():
    c = 0
    for b in bagage.keys():
        if inbag('shiny gold', b):
            c += 1
    return(c)

def countin(bag):
    inside = 0
    for b in bagage[bag]:
        inside += countin(b)
    return(inside + len(bagage[bag]))

def parttwo():
    number = countin('shiny gold')
    return(number)

print('Advent of Code 2020, day 7 part 1')
print(partone())
print('Advent of Code 2020, day 7 part 2')
print(parttwo())
