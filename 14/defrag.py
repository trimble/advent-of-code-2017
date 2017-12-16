import networkx as nx

input = ["amgozmfv-{}".format(i) for i in range(128)]

for x in list(range(128)):
    input[x] = [ord(i) for i in input[x]]
    input[x] = input[x] + [17, 31, 73, 47, 23]

def process(state, length, skip):
    copy = state
    sub = state[:length]
    sub = sub[::-1]
    for j in list(range(length)):
        state[j] = sub[j]
    return state

def rotate(myList, index):
    return myList[index:] + myList[:index]

hashed = []
for x in list(range(128)):
    current = 0
    skip = 0
    state = list(range(0,256))
    for j in list(range(64)):
        for i in input[x]:
            temp = rotate(state, current)
            process(temp, i, skip)
            state = rotate(temp, len(state)-current)
            current = (current + (i + skip)) % len(state)
            skip += 1

    dense = []
    for i in list(range(16)):
        temp = state[16*i]
        for j in list(range(1,16)):
            temp ^= state[16*i+j] 
        dense.append(temp)
    hashed.append(dense)

output = []
for y in list(range(128)):
    foo = ["{:08b}".format(i) for i in hashed[y]]
    output.append("".join(foo))

G = nx.empty_graph()
for i in list(range(128)):
    for j in list(range(128)):
        if output[i][j] == '1':
            G.add_node(i*128+j)
            if j < 127 and output[i][j+1] == '1':
                G.add_edge(i*128+j, i*128+j+1)
            if i < 127 and output[i+1][j] == '1':
                G.add_edge(i*128+j, (i+1)*128+j)


print(len(list(nx.connected_components(G))))
# count = 0
# outliers=[]
# for i in g.vertices():
#     if g.find_path(i, '0'):
#         count += 1
#     else:
#         outliers.append(str(i))
# print("number of nodes in 0's group = {}".format(count))
# print("number of nodes *not* in 0's group = {}".format(len(outliers)))
# print("first outlier = {}".format(outliers[0]))

# numGroups = 1
# while len(outliers):
#     outliers2=[]
#     count = 0
#     for i in outliers:
#         if g.find_path(i, outliers[0]):
#             count += 1
#         else:
#             outliers2.append(i)
# 
#     print("number of nodes in {}'s group = {}".format(outliers[0], count))
#     if len(outliers2):
#         print("number of nodes *not* in {}'s group = {}".format(outliers[0], len(outliers2)))
#         print("first outlier = {}".format(outliers2[0]))
#     outliers = outliers2
#     numGroups += 1
# 
# print("there are {} groups".format(numGroups))
