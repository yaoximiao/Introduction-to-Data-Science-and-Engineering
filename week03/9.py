import random

size = int(input('请输入数组规模：'))
a = []
for i in range(size):
    a.append(int(100 * random.random()))
b = []
for i in range(size):
    result = 1
    for j in range(0, i):
        result *= a[j]
    for k in range(i + 1, size):
        result *= a[k]
    b.append(result)
print(b)
