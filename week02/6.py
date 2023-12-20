# 牛顿法修改
def square_root():
    c = 2000
    g = c
    while abs(g * g - c) > 0.00000000001:
        g = (g + c / g) / 2
    print(g)


square_root()
# 实验结果：无影响，本质是不断优化的过程。类似于贝叶斯。
