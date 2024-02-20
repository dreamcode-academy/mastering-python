import numpy as np


array_to_save = np.array([1, 2, 3, 4, 5])

#np.savetxt('example.txt', array_to_save)

array_from_file = np.loadtxt('example.txt') 

#print(array_from_file)


array_to_save_binary = np.array([10, 20, 30, 40, 50])

#np.save('example.npy', array_to_save_binary)

array_from_binary_file = np.load('example.npy')

print(array_from_binary_file)