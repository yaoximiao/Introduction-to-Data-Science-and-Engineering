import re

my_license = input('请输入身份证:')
pattern = r"^(^\d{15}$)|(^\d{17}([0-9]|X)$)"
match = re.match(pattern, my_license)
if match:
    print('success')
else:
    print('fail')
