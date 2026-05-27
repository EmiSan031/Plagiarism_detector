def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value * scalar)
        result.append(new_row)
    return result

def matrix_add(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def trace(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

print(identity_matrix(3))
print(scalar_multiply([[1, 2], [3, 4]], 3))
print(matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
