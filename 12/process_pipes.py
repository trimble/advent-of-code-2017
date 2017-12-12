from graph import Graph
import re

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

state = {}
for line in content:
    print(line)
    x = re.search(r'(.*?) <-> (.*)', line)
    print("process {} connects to {}".format(x.group(1), x.group(2)))
    state[str(x.group(1))] = x.group(2).split(', ')

print(state)

graph = Graph(state)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print(graph.find_path('0', '3'))
count = 0
for i in graph.vertices():
    if graph.find_path(i, '0'):
        count += 1
print(count)
