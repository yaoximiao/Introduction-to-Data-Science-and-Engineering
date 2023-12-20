# 数论问题，假如数据分解后允许重复，则优先凑3，因为4->2*2，5->2*3,*5不如*2*3，
x = int(input('请输入待处理数：'))
result = int(x/3)
print("result="+str(result))
yu = x - result * 3
print("yu="+str(yu))
if yu == 0:
    print(3**result)
elif yu == 1:
    print(3**(result-1)*2*2)
else:
    print(3**result*2)
