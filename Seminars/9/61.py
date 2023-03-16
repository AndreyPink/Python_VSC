# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')

print(f'max of median_house_value {max(df["median_house_value"])}')
print(f'min of median_house_value {min(df["median_house_value"])}')
print('\n')
print(max(df[df['median_income'] == 3.1250]['median_house_value']))
print('\n')
print(max(df[(df['median_house_value']) == min(df['median_house_value'])]['population']))
