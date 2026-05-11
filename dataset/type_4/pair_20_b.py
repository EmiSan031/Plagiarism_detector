def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


print(transpose([[1, 2, 3], [4, 5, 6]]))
