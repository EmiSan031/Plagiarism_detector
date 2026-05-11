def transpose(matrix):
    result = []

    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        result.append(new_row)

    return result


# Matrix transpose demo.
print(transpose([[1, 2, 3], [4, 5, 6]]))
