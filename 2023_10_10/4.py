# 实现希尔排序
def insert_sort(my_integer_list, start, end, gap, upper):
    for i in range(start, end, gap):
        if i > upper:
            return
        for j in range(start, i, gap):
            if my_integer_list[j] > my_integer_list[i]:
                temp = my_integer_list[i]
                for k in range(i, j, -gap):
                    my_integer_list[k] = my_integer_list[k - gap]
                my_integer_list[j] = temp
    return
    # print(integer_list)


input_str = input('请输入数字（以空格间隔）：')
input_list = input_str.split()
integer_list = [int(x) for x in input_list]
my_gap = len(integer_list) // 2
while my_gap != 0:
    for my_i in range(my_gap):
        insert_sort(integer_list, my_i, len(integer_list), my_gap, len(integer_list))
    my_gap = my_gap // 2

print(integer_list)
