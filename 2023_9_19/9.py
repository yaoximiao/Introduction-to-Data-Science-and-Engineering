# 蒙特卡洛思想求定积分
import random
import math
import numpy as np


# 定义函数
def f(x):
    return x ** 2 + 4 * x * math.sin(x)


def monte(left, right):
    num_points = 10000000
    inputs = np.linspace(left, right, num_points)
    outputs = [f(x) for x in inputs]
    my_max = max(outputs)
    i = 0
    count = 0
    total = 1e7
    while i < total:
        x = left + (right-left)*random.random()
        y = my_max * random.random()
        if y <= f(x):
            count += 1
        i += 1
    total_area=(right-left)*my_max
    print(total_area * (right - left) * (count / total))


monte(2, 3)
