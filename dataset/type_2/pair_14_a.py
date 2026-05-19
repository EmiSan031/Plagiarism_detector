def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

def row_sums(matrix):
    sums = []
    for row in matrix:
        row_total = 0
        for value in row:
            row_total += value
        sums.append(row_total)
    return sums

def column_sums(matrix):
    num_cols = len(matrix[0])
    sums = []
    for col in range(num_cols):
        col_total = 0
        for row in matrix:
            col_total += row[col]
        sums.append(col_total)
    return sums

def matrix_report(matrix):
    print(f"Matrix contents :")
    for row in matrix:
        print(f"  {row}")
    print(f"Rows            : {len(matrix)}")
    print(f"Columns         : {len(matrix[0])}")
    total = matrix_sum(matrix)
    print(f"Total sum       : {total}")
    r_sums = row_sums(matrix)
    print(f"Row sums        : {r_sums}")
    c_sums = column_sums(matrix)
    print(f"Column sums     : {c_sums}")
    num_elements = len(matrix) * len(matrix[0])
    print(f"Average value   : {total / num_elements:.2f}")

matrix_report([[1, 2, 3], [4, 5, 6]])
