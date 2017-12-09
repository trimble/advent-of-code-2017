import re

def process(x):
    temp = re.sub(r'{.*}', 'x', content)
    return content.count('x')

content = (open('input.txt').readlines())[0]

content = content.strip()
content = re.sub(r'!.', "", content)
content = re.sub(r'<.*?>', "", content)
content = re.sub(r',', "", content)
content = re.sub(r'}{', "},{", content)

count = 1
score = 0
for i in content:
    if i == '{':
        score += count
        count += 1
    elif i == '}':
        count -= 1

print(content)
print(count)
print(score)
