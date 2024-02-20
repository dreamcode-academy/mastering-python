import numpy as np

# Create an example array
data = np.array([ 40, 10, 20, 50, 30])

sorted_array = np.sort(data)
print(sorted_array)

condition_elements = data[data > 30]
print("Condition: ", condition_elements)






total_sum = np.sum(data)
total_product = np.prod(data)
cumulative_sum = np.cumsum(data)
cumulative_product = np.cumprod(data)
'''

print("Total Sum: ", total_sum)
print("Total Product: ", total_product)
print("Cumulative Sum: ", cumulative_sum)
print("Cumulative Product: ", cumulative_product)
'''