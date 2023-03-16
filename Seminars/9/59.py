# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')

print(df.isnull().sum())
print('\n\n')
print(df[df['median_income'] < 2]['median_house_value'])
print('\n\n')
print(df.iloc[:, 0:2])
print('\n\n')
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 7000)])
