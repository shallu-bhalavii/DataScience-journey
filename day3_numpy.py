import numpy as np

# # Create a 1D array
# arr1 = np.array([1, 2, 3, 4])
# print("Array 1:", arr1)

# # Create a 2D array
# arr2 = np.array([[1, 2], [3, 4], [5, 6]])
# print("Array 2:\n", arr2)

# # Vectorized operations
# print("Array 1 + 5:", arr1 + 5) # Adding 5 to each element
# print("Array 1 * 2:", arr1 * 2) # Multiplying each
# print("Array 1 squared:", arr1**2)

# # Dot product
# arr3 = np.array([5, 6, 7, 8])
# dot_product = np.dot(arr1, arr3)
# print("Dot product:", dot_product)  # Dot product of arr1 and arr3

# # Shape and size
# print("Shape of arr2:", arr2.shape)
# print("Size of arr2:", arr2.size)

# ''' Shape of arr2: (3, 2)
#     Size of arr2: 6'''

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print("Array 1:\n", arr1)
print("Shape of arr1:", arr1.shape)

arr = np.arange(1, 21)
print(arr)

matrix = arr.reshape(4, 5)
print(matrix)


row1 = arr1[0] #first_row = matrix[0]
print("extract first row: ",row1)
# [1 2 3 4 5]


col5 = arr1[:,4:5] #col5 = arr1[:,-1]
print("extract last column: ",col5)
#[ 5 10 15 20]

midrc = arr1[1:3,1:4]
print("extract middle 2x3 subarray:\n", midrc)

arr2 = np.array([[1,45,34,67,100],[98,45,76,32,99],[31,66,11,6,87],[55,22,33,44,55]])
#rand_matrix = np.random.randint(1, 101, (4, 5))
arr3 = np.append(arr1,values=arr2, axis=0)
#sum_matrix = matrix + rand_matrix
print("Concatenated array:\n", arr3)

print("multiplication of arr1 and arr2: ",arr1*arr2)

arrm = np.mean(arr1)
arrme = np.median(arr1)
arrd = np.std(arr1)
print(f"mean: {arrm}, \nmedian: {arrme}, \nstandard deviation of arr1:{arrd} ")

arrsum = np.sum(arr1[:,0:5])
print("sum of each column:",arrsum)

max = np.max(arr3)
print(max)              # 20
max_pos = np.unravel_index(np.argmax(arr3), arr3.shape)  # (3, 4)
print("max position:", max_pos)  # (3, 4)
