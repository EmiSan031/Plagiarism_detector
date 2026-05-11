def flatten(matrix):
    return [value for row in matrix for value in row]


print(flatten([[1, 2], [3, 4], [5, 6]]))
