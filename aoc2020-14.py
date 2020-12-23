#!/usr/bin/python3
import copy
with open('aoc2020-14-input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

def partone():
    memory = {}

    def write(a, v, m):
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
        [com, _, val] = l.split(' ')
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

def parttwo():
    memory = {}

    def step(addr, value, mask, mem):
        addr = '{0:036b}'.format(addr)
        for i in range(len(mask)):
            if mask[i] == '1':
                addr = addr[:i] + '1' + addr[i+1:]
            elif mask[i] == '0':
                pass

        addresses = [addr]
        for i in range(len(mask)):
            if mask[i] == 'X':
                newlist = []
                for a in addresses:
                    n1 = a[:i] + '1' + a[i+1:]
                    n0 = a[:i] + '0' + a[i+1:]
                    newlist.append(n1)
                    newlist.append(n0)
                addresses = copy.deepcopy(newlist)

        for ad in addresses:
            mem[int(ad, base=2)] = value
        return(mem)

    for l in lines:
        [com, _, val] = l.split(' ')
        if com == 'mask':
            mask = val
        if com[:3] == 'mem':
            address = int(com.split('[')[1][:-1])
            val = int(val)
            memory = step(address, val, mask, memory)

    sum = 0
    for addr in memory.keys():
        sum += memory[addr]
    return(sum)

print('Advent of Code 2020, day 14 part 1')
print(partone())
print('Advent of Code 2020, day 14 part 2')
print(parttwo())
