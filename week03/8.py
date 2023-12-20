import timeit


# 排序算法
# 选择排序
def selection_sort(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        my_max_index = i
        for j in range(0, i):
            if my_list[j] > my_list[my_max_index]:
                my_max_index = j
        temp = my_list[i]
        my_list[i] = my_list[my_max_index]
        my_list[my_max_index] = temp
    return my_list


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def partition(my_list, left, right):
    pivot = my_list[right]
    i = left - 1
    for j in range(left, right):
        if my_list[j] < pivot:
            i += 1
            (my_list[i], my_list[j]) = (my_list[j], my_list[i])
    (my_list[i + 1], my_list[right]) = (my_list[right], my_list[i + 1])
    return i + 1


def quick_sort(my_list, left, right):
    if left < right:
        pi = partition(my_list, left, right)
        quick_sort(my_list, left, pi - 1)
        quick_sort(my_list, pi + 1, right)


a = [5, 4, 2, 1, 2]
setup_code = """
from __main__ import quick_sort, a
"""
code_to_test = """
quick_sort(a, 0, 4)
"""
execution_time = timeit.timeit(code_to_test, setup=setup_code, number=100000)
print(f"Execution time: {execution_time} seconds")
print(a)
