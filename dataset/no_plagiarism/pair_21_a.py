def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]

print(transpose([[1, 2, 3], [4, 5, 6]]))
