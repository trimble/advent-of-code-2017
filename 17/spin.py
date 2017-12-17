state = [0]
input = 337
current = 0

for i in range(1,50):
    temp = current
    state = state[current:] + state[:current]
    current = 0
    pos = input % len(state)
    state.insert(pos+1, i)
    state = state[state.index(0):] + state[:state.index(0)]
    current = state.index(i)
    print(state)

print(state.index(2017))
print(state[state.index(2017)-30:state.index(0)+3])
