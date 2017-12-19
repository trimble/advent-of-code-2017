import re
from collections import deque

def valOf(x, registers):
    if re.match(r'-?\d+', x):
        return int(x)
    else:
        return registers[x]

def runIt(process, registers, instr, addr):
    global a_waiting
    global b_waiting
    global a_queue
    global b_queue
    global a_numSnd
    global b_numSnd
    print(process, instr)
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
        if process == 'a':
            b_queue.append(valOf(x.group(2), registers))
            a_numSnd += 1
        else:
            a_queue.append(valOf(x.group(2), registers))
            b_numSnd += 1
    elif x.group(1) == 'rcv':
        if process == 'a':
            if len(a_queue):
                registers[x.group(2)] = a_queue.popleft()
                a_waiting = False
            else:
                a_waiting = True
                addr -= 1
        else:
            if len(b_queue):
                registers[x.group(2)] = b_queue.popleft()
                b_waiting = False
            else:
                b_waiting = True
                addr -= 1
    elif x.group(1) == 'jgz':
        if valOf(x.group(2), registers) > 0:
            addr += valOf(x.group(3), registers)
            addr -= 1
    return addr, registers

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

a_registers = {}
b_registers = {}
a_queue = deque([])
b_queue = deque([])
a_waiting = False
b_waiting = False
a_addr = 0
b_addr = 0
a_numSnd = 0
b_numSnd = 0

for i in content:
    x = re.match( r'(.*?) (.)(?: (.*))?', i)
    a_registers[x.group(2)] = 0
    b_registers[x.group(2)] = 0

a_registers['p'] = 0
b_registers['p'] = 1

while a_addr < len(content): #NOTE: This only works because b never runs out of instructions before it starves on the queue
    i = content[a_addr]
    j = content[b_addr]
    a_addr, a_registers = runIt('a', a_registers, i, a_addr)
    b_addr, b_registers = runIt('b', b_registers, j, b_addr)
    a_addr += 1
    b_addr += 1
    if a_waiting & b_waiting:
        break

print(a_numSnd, b_numSnd, len(a_queue), len(b_queue))
