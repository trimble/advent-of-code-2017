from collections import Counter

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def hasDuplicates(mylist):
    return [k for k,v in Counter(mylist).items() if v>1]

def validate(x):
    if hasDuplicates(x.split(' ')):
        return False
    return True

count = 0

for passphrase in content:
    if validate(passphrase):
        count += 1

print(count)
