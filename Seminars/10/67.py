# Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

import seaborn as sns
import pandas as pd

penguins = sns.load_dataset("penguins")

penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] < 42) & (penguins['bill_length_mm'] >= 35), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'

print(penguins.head())