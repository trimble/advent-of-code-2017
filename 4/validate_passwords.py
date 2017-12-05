from collections import Counter

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def hasAnagrams(mylist):
    sortedList = mylist 
    for j,i in enumerate(sortedList):
        i = list(i)
        i.sort()
        sortedList[j] = ''.join(i)
    print(sortedList)
    return [k for k,v in Counter(sortedList).items() if v>1]
    #return True

def validate(x):
    if hasAnagrams(list(x.split(' '))):
        return False
    return True

count = 0

for passphrase in content:
    if validate(passphrase):
        count += 1

print(count)
