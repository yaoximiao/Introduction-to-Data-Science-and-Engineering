import random
import math


# 蒙特卡洛模拟落点
def method1():
    total = 100000000
    need = 0
    for i in range(total):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1:
            need += 1
    result = float(need / total)
    print('%.10f' % (4 * result))


# 级数累加
def method2():
    i = 1
    k = 1
    result = 0
    while i < 100000000:
        result += (1 / i) * k
        k = -k
        i += 2
    print(result * 4)


# 使用多边形逼近
def method3():
    n = 100000000
    print(math.sin(math.radians(360 / 2 / n)) * n)


method1()
method2()
method3()
