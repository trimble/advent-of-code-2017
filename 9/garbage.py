import re

content = (open('input.txt').readlines())[0]

content = content.strip()
content = re.sub(r'!.', "", content)
print(len(content))
x = re.findall(r'(<.*?>)', content)
print(len(x))
content = re.sub(r'<.*?>', "", content)
print(len(content))
