def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)

    return transposed

# Example matrix
A = [[1, 2, 3],
     [4, 5, 6]]

# Transpose
result = transpose_matrix(A)

# Output result
for row in result:
    print(row)


"""
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)

"""