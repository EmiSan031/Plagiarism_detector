def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def scalar_multiply(matrix, scalar):
    return [[v * scalar for v in row] for row in matrix]

def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def zeros_matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

def flatten(matrix):
    return [v for row in matrix for v in row]

def is_symmetric(matrix):
    return all(
        matrix[i][j] == matrix[j][i]
        for i in range(len(matrix)) for j in range(len(matrix))
    )

print(identity_matrix(3))
print(scalar_multiply([[1, 2], [3, 4]], 3))
print(matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(zeros_matrix(2, 3))
print(is_symmetric([[1, 2], [2, 1]]))
