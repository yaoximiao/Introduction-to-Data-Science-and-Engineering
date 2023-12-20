import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', color_codes=True)
tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', hue='time', data=tips)
plt.show()
