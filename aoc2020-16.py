#!/usr/bin/python3
with open('aoc2020-16-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

spec = {}
for (i,l) in enumerate(lines):
    if l == 'your ticket:':
        my_ticket = list(map(int, lines[i+1].split(',')))
    elif l == 'nearby tickets:':
        other = []
        for row in lines[i+1:]:
            other.append(list(map(int, row.split(','))))
    elif len(l.split(':')) == 2:
        spec[l.split(':')[0].strip()] = l.split(':')[1].strip()

def partone():
    def valid(n):
        for apa in spec.keys():
            [a, b] = spec[apa].split('or')
            [a1, a2] = list(map(int, a.strip().split('-')))
            [b1, b2] = list(map(int, b.strip().split('-')))
            if (n >= a1 and n <= a2) or (n >= b1 and n <= b2):
                return(True)
        return(False)

    error = 0
    for ticket in other:
        for num in ticket:
            if valid(num):
                pass
            else:
                error += num
    return(error)

def parttwo():
    def valid(n):
        for apa in spec.keys():
            [a, b] = spec[apa].split('or')
            [a1, a2] = list(map(int, a.strip().split('-')))
            [b1, b2] = list(map(int, b.strip().split('-')))
            if (n >= a1 and n <= a2) or (n >= b1 and n <= b2):
                return(True)
        return(False)

    def field(ns):
        lista = []
        for apa in spec.keys():
            [a, b] = spec[apa].split('or')
            [a1, a2] = list(map(int, a.strip().split('-')))
            [b1, b2] = list(map(int, b.strip().split('-')))
            if all((n >= a1 and n <= a2) or (n >= b1 and n <= b2) for n in ns):
                lista.append(apa)
        return(lista)

    valid_tickets = []
    for ticket in other:
        if all(valid(num) for num in ticket):
            valid_tickets.append(ticket)
    i = 0
    order = []
    while i < len(valid_tickets[0]):
        order.append(field([item[i] for item in valid_tickets]))
        i += 1

    ordered = list(enumerate(order))
    ordered.sort(key=lambda tup: len(tup[1]))

    bös = []
    biljett = []
    for (a, bepa) in ordered:
        for b in bepa:
            if b not in bös:
                bös.append(b)
                biljett.append((a, b))

    biljett.sort()

    svaret = 1
    for (i, b) in (biljett):
        if 'departure' in b:
            svaret *= my_ticket[i]
    return(svaret)

print('Advent of Code 2020, day 16 part 1')
print(partone())
print('Advent of Code 2020, day 16 part 2')
print(parttwo())
