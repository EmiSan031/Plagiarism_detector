def transpose(matrix):
    result = []

    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        result.append(new_row)

    return result

def matrix_dimensions(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows, cols

def is_square(matrix):
    rows, cols = matrix_dimensions(matrix)
    return rows == cols

# Extract the main diagonal of the matrix.
def diagonal(matrix):
    result = []
    size = min(len(matrix), len(matrix[0]))
    for i in range(size):
        result.append(matrix[i][i])
    return result

# Matrix transpose demo.
grid = [[1, 2, 3], [4, 5, 6]]
square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(grid))
print(matrix_dimensions(grid))
print(is_square(grid))
print(is_square(square))
print(diagonal(square))
