from graph import Graph
import re

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

state = {}
for line in content:
    x = re.search(r'(.*?) <-> (.*)', line)
    state[str(x.group(1))] = x.group(2).split(', ')

graph = Graph(state)

count = 0
for i in graph.vertices():
    if graph.find_path(i, '0'):
        count += 1
print(count)
