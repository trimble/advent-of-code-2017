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
outliers=[]
for i in graph.vertices():
    if graph.find_path(i, '0'):
        count += 1
    else:
        outliers.append(i)
print("number of nodes in 0's group = {}".format(count))
print("number of nodes *not* in 0's group = {}".format(len(outliers)))
print("first outlier = {}".format(outliers[0]))

outliers2=[]
count = 0
for i in outliers:
    if graph.find_path(str(i), '1'):
        count += 1
    else:
        outliers2.append(str(i))

print("number of nodes in 1's group = {}".format(count))
print("number of nodes *not* in 1's group = {}".format(len(outliers2)))
print("first outlier = {}".format(outliers2[0]))

outliers3=[]
count = 0
for i in outliers2:
    if graph.find_path(str(i), '2'):
        count += 1
    else:
        outliers3.append(str(i))

print("number of nodes in 2's group = {}".format(count))
print("number of nodes *not* in 2's group = {}".format(len(outliers3)))
print("first outlier = {}".format(outliers3[0]))

outliers4=[]
count = 0
for i in outliers3:
    if graph.find_path(str(i), '4'):
        count += 1
    else:
        outliers4.append(str(i))

print("number of nodes in 4's group = {}".format(count))
print("number of nodes *not* in 4's group = {}".format(len(outliers4)))
print("first outlier = {}".format(outliers4[0]))

