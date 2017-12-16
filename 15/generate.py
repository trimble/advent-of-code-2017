a = 116
b = 299

a_factor = 16807
b_factor = 48271

divisor = 2147483647

count = 0
a_list = []
b_list = []
while len(a_list) < 5000000:
    a = (a * a_factor) % divisor
    if a % 4 == 0:
        a_list.append(a)

while len(b_list) < 5000000:
    b = (b * b_factor) % divisor
    if b % 8 == 0:
        b_list.append(b)

for i in list(range(5000000)):
    if (a_list[i] & 0xffff) == (b_list[i] & 0xffff):
        count += 1

print(count)
