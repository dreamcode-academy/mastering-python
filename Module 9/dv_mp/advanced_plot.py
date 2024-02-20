import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


# Create a figure for the subplots
fig, axs = plt.subplots(2, 2, figsize=(10,10))

# 3d Scatter
ax = fig.add_subplot(221, projection='3d')
z_line = np.linspace(0, 15, 1000)
x_line = np.sin(z_line)
y_line = np.cos(z_line)
ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='Greens')
axs[0, 0].axis('off')
axs[0,0].set_title("3D Scatter Plot")


# Area chart
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
axs[0, 1].fill_between(x, y1, y2)
axs[0, 1].set_title('Area Chart')


# Stacked bar chart
data1 = [5, 10, 15, 20]
data2 = [3, 6, 9, 12]
x_range = range(len(data1))
axs[1, 0].bar(x_range, data1, label='Data1')
axs[1, 0].bar(x_range, data2, bottom=data1, label='Data 2')
axs[1, 0].legend()
axs[1, 0].set_title('Stacked Bar Chart')


# Pie chart
pie_data = [30, 20, 50]
labels = ['A', 'B', 'C']
explode = (0.1, 0, 0)

axs[1, 1].pie(pie_data, labels=labels, explode=explode, autopct='%1.1f%%')
axs[1, 1].set_title("Pie Chart")

plt.tight_layout()
plt.show()
