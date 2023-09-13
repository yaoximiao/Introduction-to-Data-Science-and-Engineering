"""
numbers = []
while True:
    num_str = input("请输入数字：")
    if num_str == '':
        break
    else:
        num = int(num_str)
        numbers.append(num)
i = 1
while i < len(numbers):
    k = i-1
    while k >= 0:
        if numbers[k+1] > numbers[k]:
            t = numbers[k]
            numbers[k] = numbers[k+1]
            numbers[k+1] = t
        k -= 1
    i += 1
j = 0
while j < len(numbers):
    print(numbers[j], end=" ")
    j += 1
"""

number1 = []
while True:
    num_str1 = input("请输入数字：")
    if num_str1 == '':
        break
    else:
        num1 = int(num_str1)
        number1.append(num1)

a = len(number1)
for b in range(a):
    index = b
    for c in range(b+1, a):
        if number1[c] > number1[index]:
            index = c
    temp = number1[b]
    number1[b] = number1[index]
    number1[index] = temp
j = 0
while j < len(number1):
    print(number1[j], end=" ")
    j += 1





