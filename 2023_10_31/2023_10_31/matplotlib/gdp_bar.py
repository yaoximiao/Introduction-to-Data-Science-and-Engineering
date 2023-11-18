import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
x = df.values[:, 0]
y = df.values[:, 1]

# 使x轴显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.barh(x, width=y, height=0.8)

plt.show()
