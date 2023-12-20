def square_root():
    c = 2
    g = 0
    for j in range(0, c + 1):
        if j * j > c and g == 0:
            g = j - 1
    while abs(g * g - c) > 0.0001:
        g += 0.00001
    print(g)


square_root()
