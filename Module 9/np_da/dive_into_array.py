import numpy as np
'''
# Create a one dimensional array from list

np.array([1,2,3])
#Array attributes
#array.shape
#array.size
#array.dtype
#array.itemsize

np.array([1,2,3], dtype=np.float64)
'''
python_list = [4,5,6]
numpy_array = np.array(python_list)
print("NumPy Array: ", numpy_array)


print("Shape: ", numpy_array.shape)
print("Size: ", numpy_array.size)
print("Data Size: ", numpy_array.dtype)

numpy_2d_array = np.array([[1,2,3], [4,5,6]])

print("Multidimensional NumPy Array: ", numpy_2d_array)


print("Shape of 2D Array: ", numpy_2d_array.shape)
print("Size of 2D Array: ", numpy_2d_array.size)
print("Data Type of 2D Array: ", numpy_2d_array.dtype)

numpy_float_array = np.array([7,8,9], dtype=np.float64)
print("NumPy Float Array: ", numpy_float_array)
print("Data Type of Float Array: ", numpy_float_array.dtype)


