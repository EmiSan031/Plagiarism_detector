# Sum every value in a matrix.
def matrix_sum(matrix):
    total = 0

    for row in matrix:
        for value in row:
            total += value

    return total


print(matrix_sum([[1, 2, 3], [4, 5, 6]]))
