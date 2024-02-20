import numpy as np

# Asset weights in the portfolio
weights = np.array([0.3, 0.4, 0.3])

# Annual returns of those assets
returns = np.array([0.05, 0.12, 0.07])

#Calculating returns of those assets

portfolio_return = np.dot(weights, returns)


print("Portfolio return: ", portfolio_return)