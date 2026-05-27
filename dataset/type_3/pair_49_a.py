def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell = 0
            for k in range(cols_a):
                cell += a[i][k] * b[k][j]
            row.append(cell)
        result.append(row)
    return result

def matrix_trace(matrix):
    total = 0
    for i in range(min(len(matrix), len(matrix[0]))):
        total += matrix[i][i]
    return total

def multiply_report(a, b):
    product = multiply_matrices(a, b)
    trace = matrix_trace(product)
    print(f"Matrix A        : {a}")
    print(f"Matrix B        : {b}")
    print(f"Product A x B   :")
    for row in product:
        print(f"  {row}")
    print(f"Trace of product: {trace}")
    total = 0
    for row in product:
        for val in row:
            total += val
    print(f"Sum of product  : {total}")
    return product

multiply_report([[1, 2], [3, 4]], [[5, 6], [7, 8]])
