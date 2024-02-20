import pandas as pd

#df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [30, 25]})


#df = pd.read_csv('sales_data.csv')
#df = pd.read_excel('sales_data.xlsx')


#print(df.head())

data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

df.to_excel('output.xlsx', index=False)