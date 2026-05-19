def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

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

def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

grid = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
print(flatten(grid))
print(flatten_positive(grid))
print(matrix_max(grid))
print(matrix_sum(grid))
