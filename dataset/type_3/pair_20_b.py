def transpose(matrix):
    return [list(column) for column in zip(*matrix)]

def diagonal(matrix):
    return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]

def matrix_multiply(a, b):
    b_t = transpose(b)
    return [
        [sum(x * y for x, y in zip(row_a, col_b)) for col_b in b_t]
        for row_a in a
    ]

def zip_rows(a, b):
    return [list(map(sum, zip(ra, rb))) for ra, rb in zip(a, b)]

def col_sums(matrix):
    return [sum(col) for col in zip(*matrix)]

grid = [[1, 2, 3], [4, 5, 6]]
square = [[1, 2], [3, 4], [5, 6]]
print(transpose(grid))
print(diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(zip_rows([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(col_sums([[1, 2, 3], [4, 5, 6]]))
