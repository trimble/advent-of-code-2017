import re
from anytree import Node, RenderTree, find, LevelOrderIter

def weightof(tree):
    return sum([node.weight for node in LevelOrderIter(tree)])

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

root = Node('root', weight = 0)
for item in content:
    x = re.match(r'(.*) \((.*)\)(.*)', item)
    y = Node(x.group(1), parent = root, weight = int(x.group(2)))

for item in content:
    x = re.match(r'(.*) \((.*)\)(.*)', item)
    parent = find(root, lambda node: node.name == x.group(1))
    if x.group(3):
        for child in x.group(3)[4:].split(', '):
            child = find(root, lambda node: node.name == child) 
            child.parent = parent

#print([{node.name, weightof(node)} for node in LevelOrderIter(root)])
off = find(root, lambda node: node.name == 'tulwp')
print([{node.name, weightof(node)} for node in LevelOrderIter(off)])
