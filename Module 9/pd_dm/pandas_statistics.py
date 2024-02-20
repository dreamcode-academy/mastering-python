import pandas as pd

# Creating a sample DataFrame with sales data
data = {
    'date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'sales': [150, 200, 175, 120, 190, 210, 180, 160, 170, 200]
}
df = pd.DataFrame(data)


#Basic statistical functions

mean_sales = df['sales'].mean()
median_sales = df['sales'].median()
std_sales = df['sales'].std()
var_sales = df['sales'].var()

#Correlationa analysis
df['discounted_sales'] = df['sales'] * 0.9
correlation_matrix = df.corr()

#Time series

monthly_average = df.resample('M', on='date')['sales'].mean()

rolling_average= df['sales'].rolling(window = 5).mean()

print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Standard Deviation of Sales:", std_sales)
print("Variance of Sales:", var_sales)
print("\nCorrelation Matrix:\n", correlation_matrix)
print("\nMonthly Average Sales:\n", monthly_average)
print("\n5-day Rolling Average:\n", rolling_average)

      