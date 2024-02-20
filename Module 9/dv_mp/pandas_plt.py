import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.DataFrame({'Close': [120, 125, 130, 128, 135]})

moving_average = np.convolve(df['Close'], np.ones(2)/2, mode='valid')


padded_moving_average = np.insert(moving_average, 0, np.nan)

df['Moving Average'] =  padded_moving_average

plt.plot(df['Close'], label='Close')
plt.plot(df['Moving Average'], label='Moving Average')

plt.legend()
plt.show()

#df['Close'].plot(kind = 'line')
#plt.show()

#temperatures = np.array([22, 25, 24, 26, 23, 27, 28])
#plt.hist(temperatures, bins = 5)
#plt.show()