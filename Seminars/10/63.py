# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

import pandas as pd
import seaborn as sns
df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')
#1
sns.scatterplot(data=df, x = 'households', y = 'population')
#2
sns.relplot(data=df, x='longitude', y = 'median_house_value', kind='line')
#3
sns.histplot(data=df, x = 'housing_median_age')
#4
sns.displot(df, x="median_house_value", hue="housing_median_age")

