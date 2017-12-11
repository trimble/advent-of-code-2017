state = list(range(0,256))
input = '199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192'
#state = list(range(0,5))
#input = [3, 4, 1, 5]

input = [ord(i) for i in input]
input = input + [17, 31, 73, 47, 23]

def process(state, length, skip):
    copy = state
    sub = state[:length]
    sub = sub[::-1]
    for j in list(range(length)):
        state[j] = sub[j]
    return state

def rotate(myList, index):
    return myList[index:] + myList[:index]

current = 0
skip = 0
for j in list(range(64)):
    for i in input:
        temp = rotate(state, current)
        process(temp, i, skip)
        state = rotate(temp, len(state)-current)
        current = (current + (i + skip)) % len(state)
        skip += 1
print(state)
dense = []
for i in list(range(16)):
    temp = state[16*i]
    for j in list(range(1,16)):
        temp ^= state[16*i+j] 
    dense.append(hex(temp))
print(dense)
