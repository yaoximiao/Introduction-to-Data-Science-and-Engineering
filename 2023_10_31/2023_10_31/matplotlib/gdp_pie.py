import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
labels = df.values[:, 0]
y = df.values[:, 1]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90, labeldistance=1.1)
plt.legend(labels, loc='upper right')
plt.axis('equal')  # 确保饼图绘制为一个圆。

plt.show()
