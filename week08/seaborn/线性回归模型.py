import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置第一个样式
sns.set_style('darkgrid')
tips = sns.load_dataset('tips')
sns.lmplot(x='total_bill', y='tip', ci=60, hue='smoker', data=tips)

plt.show()
