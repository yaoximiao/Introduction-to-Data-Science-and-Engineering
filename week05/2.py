# 利用python获取程序执行的时间
import time
import math

start = time.perf_counter()


def judgement(x):
    flag = 0
    upper = int(math.sqrt(x)) + 2
    if x == 2 or x == 3:
        return flag
    for i in range(1, upper):
        if x % i == 0:
            flag = 1
            break
    return flag


number = int(input('请输入参数：'))
if judgement(number) == 1:
    print('不是质数')
else:
    print('是素数')
end = time.perf_counter()
print('程序运行时间为：%s Seconds' % (end - start))
