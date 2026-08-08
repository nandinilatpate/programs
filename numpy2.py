import numpy as np

# Create the first matrix
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

# Create the second matrix
matrix2 = np.array([
    [5, 6],
    [7, 8]
])

# Display the matrices
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Perform matrix multiplication
result = np.matmul(matrix1, matrix2)

# Display the result
print("\nMatrix Multiplication Result:")
print(result)