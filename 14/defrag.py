input = ["flqrgnkx-{}".format(i) for i in range(128)]

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
    print(foo)
    output.append("".join(foo))

aa = 0
for i in output:
    aa += i.count('1')

print(aa)
for i in output:
    print(i)
