# Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/mledu-datasets/california_housing_train.csv')

print(max(df[(df['population']) == min(df['population'])]['households']))
