import re

def valOf(x, registers):
    if re.match(r'-?\d+', x):
        return int(x)
    else:
        return registers[x]

def runIt(process, registers, instr, addr, lastSnd):
    x = re.match( r'(.*?) (.)(?: (.*))?', instr)
    if x.group(1) == 'set':
        registers[x.group(2)] = valOf(x.group(3), registers)
    elif x.group(1) == 'add':
        registers[x.group(2)] += valOf(x.group(3), registers)
    elif x.group(1) == 'mul':
        registers[x.group(2)] *= valOf(x.group(3), registers)
    elif x.group(1) == 'mod':
        registers[x.group(2)] = registers[x.group(2)] % valOf(x.group(3), registers)
    elif x.group(1) == 'snd':
        lastSnd = valOf(x.group(2), registers)
    elif x.group(1) == 'rcv':
        if valOf(x.group(2), registers):
            print(lastSnd)
            return 'xxxx'
        else:
            print('{} not > 0'.format(valOf(x.group(2))))
    elif x.group(1) == 'jgz':
        if valOf(x.group(2), registers) > 0:
            addr += valOf(x.group(3), registers)
            addr -= 1
    return addr, registers, lastSnd

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

a_registers = {}
b_registers = {}
a_addr = 0
b_addr = 0
lastSnd = 0

for i in content:
    x = re.match( r'(.*?) (.)(?: (.*))?', i)
    a_registers[x.group(2)] = 0
    b_registers[x.group(2)] = 0

#a_registers['p'] = 0
#b_registers['p'] = 1

while a_addr < len(content):
    i = content[a_addr]
    print(i)
    a_addr, a_registers, lastSnd = runIt('a', a_registers, i, a_addr, lastSnd)
    a_addr += 1

