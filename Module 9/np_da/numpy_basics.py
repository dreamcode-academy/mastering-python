import numpy as np

python_list = [1,2,3,4,5]

numpy_array = np.array([1,2,3,4,5])

doubled_python_list = [x * 2 for x in python_list]

doubled_numpy_array = numpy_array * 2

print('Python List: ', doubled_python_list)

print('NumPy Array: ', doubled_numpy_array)