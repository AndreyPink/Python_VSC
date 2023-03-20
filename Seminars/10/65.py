# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

# Чтобы подключить датасет с
# пингвинами, воспользуйтесь данным
# скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()

import seaborn as sns
import pandas as pd

penguins = sns.load_dataset("penguins")
#print(penguins.head())

#1,2
sns.scatterplot(data=penguins, x = 'body_mass_g', y = 'bill_length_mm', hue = 'sex')
sns.scatterplot(data=penguins, x = 'body_mass_g', y = 'flipper_length_mm', hue = 'sex')
sns.scatterplot(data=penguins, x = 'flipper_length_mm', y = 'bill_length_mm', hue = 'sex')

#3
sns.pairplot(penguins, hue='sex') 

#4,5
data1 = penguins[['flipper_length_mm', 'body_mass_g']]
data2 = penguins[['bill_length_mm', 'bill_depth_mm']]

sns.heatmap(data1)
sns.heatmap(data2)