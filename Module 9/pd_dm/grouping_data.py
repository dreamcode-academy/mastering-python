import pandas as pd

# Sample DataFrame with sales data
data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-02'],
    'region': ['East', 'West', 'East', 'West'],
    'sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)


grouped_data = df.groupby('region')

total_sales_per_region = grouped_data['sales'].sum()

print("Total Sales Per Region: \n", total_sales_per_region)