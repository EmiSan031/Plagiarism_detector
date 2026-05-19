def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)

def matrix_max(matrix):
    return max(max(row) for row in matrix)

def matrix_min(matrix):
    return min(min(row) for row in matrix)

def row_sums(matrix):
    return list(map(sum, matrix))

def col_sums(matrix):
    return [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]

def matrix_average(matrix):
    flat = [v for row in matrix for v in row]
    return sum(flat) / len(flat)

def matrix_range(matrix):
    return matrix_max(matrix) - matrix_min(matrix)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_sum(grid))
print(matrix_max(grid))
print(matrix_min(grid))
print(row_sums(grid))
print(col_sums(grid))
print(matrix_average(grid))
print(matrix_range(grid))
