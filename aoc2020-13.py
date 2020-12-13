#!/usr/bin/python3
with open('aoc2020-13-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

#lines = [939, '7,13,x,x,59,x,31,19']

time = int(lines[0])
buses = lines[1].split(',')

def waittime(t, line):
    wait = line - (t % line)
    return(wait, line)

def partone():
    waiting = []
    for b in buses:
        if b != 'x':
            waiting.append(waittime(time, int(b)))
    (t, l) = min(waiting)
    return(t*l)

print('Advent of Code 2020, day 13 part 1')
print(partone())
#print('Advent of Code 2020, day 13 part 2')
#print(parttwo())
