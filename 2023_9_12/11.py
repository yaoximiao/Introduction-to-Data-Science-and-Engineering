str2 = input()
str1 = []
for i in range(len(str2)-1):
    if str2[i] != ' ':
        str1.append(str2[i])
str3 = ''.join(str1)
print(str3)
