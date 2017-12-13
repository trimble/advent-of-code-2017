import re

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

board = {}
for i in content:
    x = re.search(r'(.*?): (.*)', i)
    board[str(x.group(1))] = int(x.group(2))

print(board)

score = 0
for i in range(97):
    depth = board.get(str(i))
    print("i = {}, depth = {}".format(i, depth))
    if depth:
        print(i % (2*depth-2))
        if (i % (2*depth-2) == 0):
            print("caught in layer {}".format(i))
            score += (i * depth)

print(score)
