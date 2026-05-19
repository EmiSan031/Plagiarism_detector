def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

def matrix_max(matrix):
    maximum = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > maximum:
                maximum = value
    return maximum

def matrix_min(matrix):
    minimum = matrix[0][0]
    for row in matrix:
        for value in row:
            if value < minimum:
                minimum = value
    return minimum

def row_sums(matrix):
    result = []
    for row in matrix:
        row_total = 0
        for value in row:
            row_total += value
        result.append(row_total)
    return result

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum(grid))
print(matrix_max(grid))
print(matrix_min(grid))
print(row_sums(grid))
