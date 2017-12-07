import re
from collections import defaultdict

def tree(): return defaultdict(tree)

towers = tree()

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
notBottom = []
for index, item in enumerate(content):
    x = re.match(r'(.*) (\(.*\))(.*)', item)
    content[index] = [x.group(1), x.group(2), x.group(3)]
    if x.group(3):
        notBottom.append(x.group(3)[4:].split(', '))

notBottom = [item for sublist in notBottom for item in sublist]
for item in content:
    if item[0] not in notBottom:
        print(f"Bottom candidate: {item[0]}")
        towers[item[0]]

