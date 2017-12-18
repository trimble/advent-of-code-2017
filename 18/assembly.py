import re

def valOf(x):
    if re.match(r'-?\d+', x):
        return int(x)
    else:
        return registers[x]

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

registers = {}
lastSnd = 0
addr = 0
for i in content:
    x = re.match( r'(.*?) (.)(?: (.*))?', i)
    registers[x.group(2)] = 0

while addr < len(content):
    i = content[addr]
    x = re.match( r'(.*?) (.)(?: (.*))?', i)
    print('addr = {}, instr = {}'.format(addr, x.group()))
    if x.group(1) == 'set':
        registers[x.group(2)] = valOf(x.group(3))
    elif x.group(1) == 'add':
        registers[x.group(2)] += valOf(x.group(3))
    elif x.group(1) == 'mul':
        registers[x.group(2)] *= valOf(x.group(3))
    elif x.group(1) == 'mod':
        registers[x.group(2)] = registers[x.group(2)] % valOf(x.group(3))
    elif x.group(1) == 'snd':
        lastSnd = valOf(x.group(2))
    elif x.group(1) == 'rcv':
        if valOf(x.group(2)):
            print(lastSnd)
            break
        else:
            print('{} not > 0'.format(valOf(x.group(2))))
    elif x.group(1) == 'jgz':
        if valOf(x.group(2)) > 0:
            addr += valOf(x.group(3))
            addr -= 1
    addr += 1

