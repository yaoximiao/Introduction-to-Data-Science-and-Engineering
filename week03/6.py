score = int(input("请输入成绩（整数）："))
if score < 60:
    print('不合格')
elif score <= 74:
    print('合格')
elif score <= 89:
    print('良好')
else:
    print('优秀')
   