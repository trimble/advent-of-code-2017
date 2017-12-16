import re

state = 'abcdefghijklmnop'
#state = 'abcde'

length = len(state)

with open('input.txt') as f:
#with open('test.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

steps = content[0].split(',')

def dance(state, steps):
    for step in steps:
        if step[0] == 's':
            cut = length - int(step[1:])
            state = state[cut:] + state[:cut]
        if step[0] == 'x':
            y = re.match(r'x(.*?)/(.*)', step)
            foo = list(state)
            temp = foo[int(y.group(1))]
            foo[int(y.group(1))] = foo[int(y.group(2))]
            foo[int(y.group(2))] = temp
            state = ''.join(foo)
        if step[0] == 'p':
            y = re.match(r'p(.*?)/(.*)', step)
            a = y.group(1)
            b = y.group(2)
            foo = list(state)
            first = foo.index(a)
            second = foo.index(b)
            foo[first] = b
            foo[second] = a
            state = ''.join(foo)
            
    return(state)

i=0
while i < 1000000000:
    state = dance(state, steps)
    if i % 100 == 0:
       print(i)
    i += 1

print(state)
