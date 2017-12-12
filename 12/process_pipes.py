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

numGroups = 1
while len(outliers):
    outliers2=[]
    count = 0
    for i in outliers:
        if graph.find_path(str(i), outliers[0]):
            count += 1
        else:
            outliers2.append(str(i))
    
    print("number of nodes in {}'s group = {}".format(outliers[0], count))
    if len(outliers2):
        print("number of nodes *not* in {}'s group = {}".format(outliers[0], len(outliers2)))
        print("first outlier = {}".format(outliers2[0]))
    outliers = outliers2
    numGroups += 1

print("there are {} groups".format(numGroups))
