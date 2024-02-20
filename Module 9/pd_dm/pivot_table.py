import pandas as pd

# Sample DataFrame with sales data
data = {
    'region': ['East', 'West', 'East', 'West'],
    'product': ['Product A', 'Product B', 'Product A', 'Product B'],
    'sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

pivot_table = df.pivot_table(values='sales', index='region', columns='product', aggfunc='mean')


print("Pivot Table: \n", pivot_table)

cross_tab = pd.crosstab(df['region'], df['product'])

print("\nCross Tabulation: \n", cross_tab)