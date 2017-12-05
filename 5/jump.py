with open('input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

address = 0
count = 0
while address < len(content) and address >= 0:
    print(f"address {address} = {content[address]}")
    oldVal = content[address]
    if oldVal >= 3:
        content[address] -= 1
    else:
        content[address] +=1
    address += oldVal
    count += 1

print(count)
