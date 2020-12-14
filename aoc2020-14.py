#!/usr/bin/python3
with open('aoc2020-14-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

memory = {}
def partone():
    def write(a, v, m):
        global memory
        v = str("{0:b}".format(v))
        new =''
        for i in range(1, len(m)+1):
            if m[-i] == 'X':
                if i > len(v):
                    new = '0' + new
                else:
                    new = v[-i] + new
            else:
                new = m[-i] + new
        memory[a] = new

    for l in lines:
        com = l.split(' ')[0]
        val = l.split(' ')[2]
        if com == 'mask':
            mask = val
        if com[:3] == 'mem':
            address = int(com.split('[')[1][:-1])
            val = int(val)
            write(address, val, mask)

    sum = 0
    for addr in memory.keys():
        sum += int(memory[addr], base=2)
    return(sum)

print('Advent of Code 2020, day 14 part 1')
print(partone())
#print('Advent of Code 2020, day 14 part 2')
#print(parttwo())
