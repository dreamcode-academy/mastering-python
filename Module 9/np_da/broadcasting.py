import numpy as np

#Add two arrays

a = np.array([1,2,3])

b = np.array([4,5,6])


#print(a + b)

# Broadcasting enables operations on arrays of different shapes.

a = np.array([1, 2, 3])
b = 2 

print(a * b) # Array-to-Scalar multiplication

# Broadcasting rules ensure compatibility.
# If a has shape (3,) 
a = np.array([1,2,3])

# If b has shape (1,)
b = np.array([2])

#print(a * b) # Array-to-Array multiplication






