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

def matrix_average(matrix):
    total = matrix_sum(matrix)
    count = 0
    for row in matrix:
        count += len(row)
    return total / count

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum(grid))
print(matrix_max(grid))
print(matrix_min(grid))
print(matrix_average(grid))
