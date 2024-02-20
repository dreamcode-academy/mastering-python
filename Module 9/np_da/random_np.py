import numpy as np


dice_rolls = np.random.randint(1,7,size=10)

#print("Dice rolls: ", dice_rolls)



stock_returns = np.random.normal(0.05, 0.1, 365)

#print("Stock returns: ", stock_returns)


# Time series

stock_prices = np.random.uniform(100,200,365)

daily_changes = np.diff(stock_prices)
#print('Daily changes: ', daily_changes)


cumulative_returns = np.cumsum(stock_returns)
print('Cumulative returns: ', cumulative_returns)
