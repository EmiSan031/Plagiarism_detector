def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result


print(flatten([[1, 2], [3, 4], [5, 6]]))
