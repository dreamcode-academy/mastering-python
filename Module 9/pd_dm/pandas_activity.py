import pandas as pd

df = pd.read_csv('sales_data.csv')

high_sales = df[df['sales'] > 500]

high_sales_sorted = high_sales.sort_values(by='date')

print("High sales sorted by date: \n", high_sales_sorted)

df['tax'] = df['sales'].apply(lambda x: x * 0.1)

print("\nDataFrame with tax column: \n", df)


df['total_cost'] = df['sales'] + df['tax']
print("\nDataFrame with total cost column: \n", df)
