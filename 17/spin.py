state = [0]
input = 337
current = 0

for i in range(1, 50000001):
    current = ((current + input) % i) + 1
    if current == 1:
        last_1 = i

print(last_1)
