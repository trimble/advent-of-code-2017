import re

def process(x, highest):
    y = re.match( r'(.*?) (.*)', x.group(2))
    if y.group(1) == 'inc':
        registers[x.group(1)] += int(y.group(2))
    else:
        registers[x.group(1)] -= int(y.group(2))
    return max(registers[x.group(1)], highest)

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

registers = {}
highest = 0
for i in content:
    x = re.match( r'(.*?) (.*?) if (.*)', i)
    registers[x.group(1)] = 0

for i in content:
    x = re.match( r'(.*?) (.*?) if (.*)', i)
    y = re.match( r'(.*?) (.*?) (.*)', x.group(3))
    if y.group(2) == '==':
        if registers[y.group(1)] == int(y.group(3)):
            highest = process(x, highest)
    elif y.group(2) == '>':
        if registers[y.group(1)] > int(y.group(3)):
            highest = process(x, highest)
    elif y.group(2) == '>=':
        if registers[y.group(1)] >= int(y.group(3)):
            highest = process(x, highest)
    elif y.group(2) == '<':
        if registers[y.group(1)] < int(y.group(3)):
            highest = process(x, highest)
    elif y.group(2) == '<=':
        if registers[y.group(1)] <= int(y.group(3)):
            highest = process(x, highest)
    elif y.group(2) == '!=':
        if registers[y.group(1)] != int(y.group(3)):
            highest = process(x, highest)

print(max([registers[i] for i in registers]))
print(highest)
