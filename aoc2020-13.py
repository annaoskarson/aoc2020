#!/usr/bin/python3
with open('aoc2020-13-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

#lines = [939, '7,13,x,x,59,x,31,19'] #1068781
#lines = [0, '17,x,13,19'] #3417
#lines = [0, '67,7,59,61'] #754018
#lines = [0, '67,x,7,59,61'] #779210
#lines = [0, '67,7,x,59,61'] #1261476
#lines = [0, '1789,37,47,1889'] #1202161486

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

def checkbuses(t, timetable):
    for (time, ID) in timetable:
        if (t + time) % ID != 0:
            return(False)
    return(True)

def parttwo():
    hitlist = []
    for (i, b) in enumerate(buses):
        if b != 'x':
            hitlist.append((i,int(b)))
    (t1, ID1) = hitlist[0]
    i = 1
    t = ID1 - t1
    dt = 1

    while i <= len(hitlist):
        if checkbuses(t, hitlist):
            return(t)
        if checkbuses(t, hitlist[:i]):
            (_, bt) = hitlist[i-1]
            dt *= bt
            i += 1
        t += dt
    return(0) #Something went wrong ...

print('Advent of Code 2020, day 13 part 1')
print(partone())
print('Advent of Code 2020, day 13 part 2')
print(parttwo())
