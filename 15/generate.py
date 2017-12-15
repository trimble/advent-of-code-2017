a = 116
b = 299

a_factor = 16807
b_factor = 48271

divisor = 2147483647

count = 0
a_list = []
b_list = []
for i in list(range(40000000)):
    a = (a * a_factor) % divisor
    b = (b * b_factor) % divisor
    a_list.append(a)
    b_list.append(b)
    if (a & 0xffff) == (b & 0xffff):
        count += 1

print(count)
