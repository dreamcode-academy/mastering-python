#
import pandas as pd

data = {'Column1': [1, 2, None, 4], 'Column2': [None, 2, 3, 4]}

df = pd.DataFrame(data)

#Forward fill
df_forward_filled = df.fillna(method = 'ffill')


#Backward Fill
df_backward_filled = df.fillna(method = 'bfill')

print("Original DataFrame:\n", df)

print("\nDataFrame after Forward Fill:\n", df_forward_filled)

print("\nDataFrame after Backward Fill:\n", df_backward_filled)
