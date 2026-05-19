def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

def matrix_dimensions(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows, cols

def flatten_positive(matrix):
    result = []
    for row in matrix:
        for value in row:
            if value > 0:
                result.append(value)
    return result

def matrix_max(matrix):
    flat = flatten(matrix)
    maximum = flat[0]
    for value in flat:
        if value > maximum:
            maximum = value
    return maximum

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(grid))
print(matrix_dimensions(grid))
print(flatten_positive([[-1, 2], [3, -4], [5, 6]]))
print(matrix_max(grid))
