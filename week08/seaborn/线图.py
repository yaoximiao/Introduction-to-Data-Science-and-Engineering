import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
fmri = sns.load_dataset('fmri')
sns.relplot(x='timepoint', y='signal', hue='event', style='event', col='region', kind='line', data=fmri)
plt.show()
