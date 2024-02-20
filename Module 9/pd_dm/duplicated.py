#
import pandas as pd

#df.duplicated().sum()

#df.drop_duplicates()

df = pd.read_csv('sample_data.csv')

df = df.drop_duplicates(['Customer'])

print(df.head())