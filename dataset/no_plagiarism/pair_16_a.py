def matrix_trace(matrix):
    total = 0
    for index in range(min(len(matrix), len(matrix[0]))):
        total += matrix[index][index]
    return total

print(matrix_trace([[1, 2], [3, 4]]))
