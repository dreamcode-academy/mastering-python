import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.rand(10)
data2 = np.random.rand(10)
data3 = np.random.rand(10)
data4 = np.random.rand(10)


fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0, 0].plot(data1)
ax[0, 0].set_title('Subplot 1')

ax[0, 1].plot(data2)
ax[0, 1].set_title('Subplot 2')

ax[1, 0].plot(data3)
ax[1, 0].set_title('Subplot 3')

ax[1, 1].plot(data4)
ax[1, 1].set_title('Subplot 4')

plt.tight_layout()
plt.show()