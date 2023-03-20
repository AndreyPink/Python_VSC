# Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ

import seaborn as sns
import pandas as pd

penguins = sns.load_dataset("penguins")

penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] < 42) & (penguins['bill_length_mm'] >= 35), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'

print(penguins.head())

sns.histplot(penguins, x = 'flipper_length_mm', hue= 'height_group')