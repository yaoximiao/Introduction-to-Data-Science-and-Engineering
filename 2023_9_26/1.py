# 完成十到二进制小数的转换
from decimal import Decimal

number = Decimal(input('请输入十进制数：'))
int_number = int(number)
after_point = number - Decimal(int_number)  # 将整数部分转换为 Decimal 类型
b = []
o_int_number = int(int_number)
while o_int_number != 0:
    b.append(str(o_int_number % 2))
    o_int_number //= 2
i = 1
pb = []
while after_point != Decimal(0) and i < 32:  # 将0转换为 Decimal 类型
    if after_point - Decimal(2) ** Decimal(-i) >= Decimal(0):  # 将2和i转换为 Decimal 类型
        after_point -= Decimal(2) ** Decimal(-i)
        pb.append('1')
    else:
        pb.append('0')
    i += 1
print("二进制整数部分：", ''.join(reversed(b)))
print("二进制小数部分：", ''.join(pb))

# 不是计算机系统中的小数二进制表示方法
