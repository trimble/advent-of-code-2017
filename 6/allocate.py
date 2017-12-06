state = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
#state = [0,2,7,0]

def realloc(x, index, blocks):
    print("Starting with {} blocks, at {}, in {}".format(blocks, index, x))
    while blocks > 0:
        if index >= len(x):
            index = 0
        x[index] += 1
        index += 1
        blocks -= 1
    return x, blocks

count = 1
seen = []
while '-'.join(map(str,state)) not in seen:
    seen.append('-'.join(map(str,state)))
    m = max(state)
    maxes=[i for i, j in enumerate(state) if j == m]
    print(state)
    index = min(maxes)
    blocks = state[index]
    state[index] = 0
    index += 1
    state, blocks = realloc(state, index, blocks)
    count += 1
print(state)
print("Repeat after {} passes!".format(count-1))
