# 直接插入排序算法

input_str = input('请输入整数数组（用空格分割）：')
input_list = input_str.split()
integer_list = [int(x) for x in input_list]
for i in range(1, len(integer_list)):
    for j in range(i):
        if integer_list[j] > integer_list[i]:
            temp = integer_list[i]
            for k in range(i, j, -1):
                integer_list[k] = integer_list[k - 1]
            integer_list[j] = temp
print(integer_list)
