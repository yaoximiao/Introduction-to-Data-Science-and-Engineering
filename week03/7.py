# 求两个正整数的最大公约数
a = int(input('请输入整数：'))
b = int(input('请输入整数：'))
if a < b:
    t = a
    a = b
    b = t
while a % b != 0:
    temp = a % b
    a = b
    b = temp

print('最大公约数:', b)
