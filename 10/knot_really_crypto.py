state = list(range(0,256))
input = [199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192]
#state = list(range(0,5))
#input = [3, 4, 1, 5]

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
for i in input:
    temp = rotate(state, current)
    print(f"temp={temp}")
    process(temp, i, skip)
    print(f"processed={temp}")
    state = rotate(temp, len(state)-current)
    print(f"state={state}")
    current = (current + (i + skip)) % len(state)
    print(current)
    skip += 1
print(state)
print(state[0]*state[1])
