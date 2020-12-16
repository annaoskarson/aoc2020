#!/usr/bin/python3
with open('aoc2020-16-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

#print(lines)
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

    #valid_tickets = []
    #not_valid_tickets = []
    #for ticket in other:
        #if all(valid(num) for num in ticket):
            #valid_tickets.append(ticket)
    #print(len(valid_tickets), len(other))

print('Advent of Code 2020, day 16 part 1')
print(partone())
#print('Advent of Code 2020, day 14 part 2')
#print(parttwo())
