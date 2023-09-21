def tri_root():
    c = 2
    g1 = c / 2
    g2 = c
    while abs(g1 - g2) > 0.00000000001:
        t = g2
        g2 = (2 / 3) * g1 + c / (3 * g1 ** 2)
        g1 = t
    print(g1)


tri_root()
