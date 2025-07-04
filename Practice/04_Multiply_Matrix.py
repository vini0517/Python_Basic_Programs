def multiply_matrices(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(p)] for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Multiply
C = multiply_matrices(A, B)

# Output result
for row in C:
    print(row)

"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.matmul(A, B)
print(C)

"""