def transpose(matrix):
    result = []
    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        result.append(new_row)
    return result

def diagonal(matrix):
    result = []
    size = min(len(matrix), len(matrix[0]))
    for i in range(size):
        result.append(matrix[i][i])
    return result

def matrix_multiply(a, b):
    rows_a = len(a)
    cols_b = len(b[0])
    cols_a = len(a[0])
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result

grid = [[1, 2, 3], [4, 5, 6]]
square = [[1, 2], [3, 4], [5, 6]]
print(transpose(grid))
print(diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
