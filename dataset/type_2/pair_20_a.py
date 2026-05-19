def transpose(matrix):
    result = []
    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        result.append(new_row)
    return result

def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

def print_matrix(matrix, label):
    print(f"{label}:")
    for row in matrix:
        print(f"  {row}")

def transpose_report(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = transpose(matrix)
    print_matrix(matrix, "Original matrix")
    print(f"Original shape  : {rows} rows x {cols} columns")
    print_matrix(transposed, "Transposed matrix")
    print(f"Transposed shape: {cols} rows x {rows} columns")
    original_sum = matrix_sum(matrix)
    transposed_sum = matrix_sum(transposed)
    print(f"Original sum    : {original_sum}")
    print(f"Transposed sum  : {transposed_sum}")
    print(f"Sums match      : {original_sum == transposed_sum}")

transpose_report([[1, 2, 3], [4, 5, 6]])
