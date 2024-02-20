#df.isnull().sum
import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, None, 30,35],
    'City': ['New York', 'Paris', None,'London']
}

df = pd.DataFrame(data)

missing_values = df.isnull().sum()

#print("Missing values in each column: \n", missing_values)

df_filled = df.fillna('Unknown')

df_dropped = df.dropna()

#print("\nDataFrame with missing values filled:\n", df_filled)

#print("\nDataFrame with rows with missing values dropped: \n", df_dropped)

df['Age'] = df['Age'].astype('float')

print("\nDataFrame with 'Age column converted to float : \n", df)


selected_column = df['Name']

print("\nSelected Column - 'Name': \n", selected_column)

filtered_rows = df[df['Age'] > 30]

print("\nRows where 'Age' is greater than 30:\n", filtered_rows)

sorted_df = df.sort_values(by='Age')
print("\nDataFrae sorted by 'Age':\n", sorted_df)