import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
palette=sns.color_palette('muted')

tips = sns.load_dataset('tips')
sns.stripplot(x='day', y='total_bill', data=tips,palette=palette)
plt.show()
