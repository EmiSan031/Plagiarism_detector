def flatten(matrix):
    return [value for row in matrix for value in row]

def flatten_positive(matrix):
    return [value for row in matrix for value in row if value > 0]

def matrix_max(matrix):
    return max(value for row in matrix for value in row)

def matrix_sum(matrix):
    return sum(value for row in matrix for value in row)

def flatten_unique(matrix):
    return list(dict.fromkeys(v for row in matrix for v in row))

def matrix_count_positive(matrix):
    return sum(1 for row in matrix for v in row if v > 0)

grid = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
print(flatten(grid))
print(flatten_positive(grid))
print(matrix_max(grid))
print(matrix_sum(grid))
print(flatten_unique([[1, 2], [2, 3], [3, 4]]))
print(matrix_count_positive(grid))
