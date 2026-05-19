def flatten(matrix):
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

def matrix_stats(matrix):
    flat = flatten(matrix)
    total = 0
    for v in flat:
        total += v
    minimum = flat[0]
    maximum = flat[0]
    for v in flat:
        if v < minimum:
            minimum = v
        if v > maximum:
            maximum = v
    return total, minimum, maximum

def flatten_report(matrix):
    print(f"Original matrix :")
    for row in matrix:
        print(f"  {row}")
    print(f"Rows            : {len(matrix)}")
    print(f"Columns         : {len(matrix[0])}")
    flat = flatten(matrix)
    print(f"Flattened list  : {flat}")
    print(f"Total elements  : {len(flat)}")
    total, minimum, maximum = matrix_stats(matrix)
    print(f"Sum of elements : {total}")
    print(f"Minimum value   : {minimum}")
    print(f"Maximum value   : {maximum}")
    print(f"Average value   : {total / len(flat):.2f}")

flatten_report([[1, 2], [3, 4], [5, 6]])
