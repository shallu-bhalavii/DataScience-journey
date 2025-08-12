import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4])
print("Array 1:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print("Array 2:\n", arr2)

# Vectorized operations
print("Array 1 + 5:", arr1 + 5) # Adding 5 to each element
print("Array 1 * 2:", arr1 * 2) # Multiplying each
print("Array 1 squared:", arr1**2)

# Dot product
arr3 = np.array([5, 6, 7, 8])
dot_product = np.dot(arr1, arr3)
print("Dot product:", dot_product)  # Dot product of arr1 and arr3

# Shape and size
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)

''' Shape of arr2: (3, 2)
    Size of arr2: 6'''
