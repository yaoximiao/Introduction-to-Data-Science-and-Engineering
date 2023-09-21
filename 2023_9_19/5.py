# 牛顿法
def square_root():
    c = 2000
    g = c / 2
    while abs(g * g - c) > 0.00000000001:
        g = (g + c / g) / 2
    print(g)


square_root()
