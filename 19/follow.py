import re

with open('input.txt') as f:
    content = f.readlines()
content = [x.rstrip('\n') for x in content]

for i, j in enumerate(content):
    content[i] = list(j)

position = {'x':0, 'y':content[0].index('|')}
move = {'x': 1, 'y': 0}
string = []
char = content[position['x']][position['y']] 
count = 0

print('start = {}'.format(position))

while char != 'S':
    while not re.match(r'[\+S]', char):
        if re.match(r'[A-Z]', char):
            string.append(char)
        print(char)
        position['x'] += move['x']
        position['y'] += move['y']
        char = content[position['x']][position['y']] 
        count += 1
    
    if move['x']:
        if position['y'] > 0 and re.match(r'[\-A-Z]', content[position['x']][position['y']-1]):
            move = {'x': 0, 'y': -1}
        else:
            move = {'x': 0, 'y': 1}
    else:
        if position['x'] > 0 and re.match(r'[\|A-Z]', content[position['x']-1][position['y']]):
            move = {'x': -1, 'y': 0}
        else:
            move = {'x': 1, 'y': 0}
    
    if char != 'S':
        char = '.'
    print(char)

print('end = {}'.format(position))
print('move = {}'.format(move))
print(string + list(char))
print(count+1)
