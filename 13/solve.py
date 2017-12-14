import re

with open('test.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

board = {}
for i in content:
    x = re.search(r'(.*?): (.*)', i)
    board[str(x.group(1))] = int(x.group(2))

caught = True
delay = 0
while caught:
    caught = False 
    for i in range(97):
        step = i + delay
        depth = board.get(str(i))
        if depth:
            if (step % (2*depth-2) == 0):
                print("delay = {}, caught in layer {}".format(delay, i))
                caught = True
                break
    delay += 1

print(delay)
