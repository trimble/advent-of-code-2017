with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

grid=[]
for i in range(1000):
    x = []
    for j in range(1000):
        x.append('C')
    grid.append(x)

for index, i in enumerate(content):
    for k, j in enumerate(i):
        if j == '#':
            grid[index+500][k+500] = 'I'

position = [512, 512]
direction = [-1, 0]

count = 0
for i in range(10000000):
    if grid[position[0]][position[1]] == 'I':
        grid[position[0]][position[1]] = 'F'
    elif grid[position[0]][position[1]] == 'F':
        grid[position[0]][position[1]] = 'C'
    elif grid[position[0]][position[1]] == 'C':
        grid[position[0]][position[1]] = 'W'
    elif grid[position[0]][position[1]] == 'W':
        grid[position[0]][position[1]] = 'I'
        count += 1

    if grid[position[0]][position[1]] == 'W':
        if direction == [-1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, 1]
        else:
            direction = [-1, 0]
    elif grid[position[0]][position[1]] == 'F':
        if direction == [-1, 0]:
            direction = [0, 1]
        elif direction == [0, 1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, -1]
        else:
            direction = [-1, 0]
    elif grid[position[0]][position[1]] == 'C':
        if direction == [-1, 0]:
            direction = [1, 0]
        elif direction == [0, 1]:
            direction = [0, -1]
        elif direction == [1, 0]:
            direction = [-1, 0]
        else:
            direction = [0, 1]

    position[0] += direction[0]
    position[1] += direction[1]

print(count)
