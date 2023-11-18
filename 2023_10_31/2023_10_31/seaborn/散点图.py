import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
tips = sns.load_dataset('tips')
sns.relplot(x='total_bill', y='tip', hue='day', row='time', col='sex', data=tips)
plt.show()
