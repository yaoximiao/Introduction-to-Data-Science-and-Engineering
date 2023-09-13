x = input("x的值为：")
y = input("y的值为：")
z = input("z的值为：")
if x < y:
    if y < z:
        print(x, y, z)
    else:
        print(x, z, y)
else:
    if x < z:
        print(y,x,z)
    else:
        print(y, z, x)



