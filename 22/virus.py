import re

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

grid=[]
for i in range(1000):
    x = []
    for j in range(1000):
        x.append(False)
    grid.append(x)

for index, i in enumerate(content):
    for k, j in enumerate(i):
        if j == '#':
            grid[index+500][k+500] = True

position = [512, 512]
direction = [-1, 0]

count = 0
for i in range(10000):
    if grid[position[0]][position[1]]:
        grid[position[0]][position[1]] = False
    else:
        grid[position[0]][position[1]] = True
        count += 1

    if grid[position[0]][position[1]]:
        if direction == [-1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, 1]
        else:
            direction = [-1, 0]
    else:
        if direction == [-1, 0]:
            direction = [0, 1]
        elif direction == [0, 1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, -1]
        else:
            direction = [-1, 0]

    position[0] += direction[0]
    position[1] += direction[1]

print(count)
