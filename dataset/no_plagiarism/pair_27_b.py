def diagonal_difference(matrix):
    left = 0
    right = 0
    size = len(matrix)
    for index in range(size):
        left += matrix[index][index]
        right += matrix[index][size - index - 1]
    return abs(left - right)

print(diagonal_difference([[1, 2], [3, 4]]))
