n = float(input("请输入数字"))
x = 1.0
while True:
    y = (2/3) * x + n / (3 * x * x)
    if abs(x-y) < 0.0000001:
        break
    x = y
print(x)

