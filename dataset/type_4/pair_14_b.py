def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)


print(matrix_sum([[1, 2, 3], [4, 5, 6]]))
