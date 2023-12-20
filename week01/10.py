str1 = input()
i = 0
flag = False
for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        flag = True
        break
print(flag)
