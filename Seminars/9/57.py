# Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')
print(df.shape)
print(df.dtypes)