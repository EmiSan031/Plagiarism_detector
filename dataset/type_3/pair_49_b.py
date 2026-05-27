def mat_multiply(grid_x, grid_y):
    r_x = len(grid_x)
    c_x = len(grid_x[0])
    c_y = len(grid_y[0])
    if c_x != len(grid_y):
        return None
    output = []
    for i in range(r_x):
        line = []
        for j in range(c_y):
            entry = 0
            for k in range(c_x):
                entry += grid_x[i][k] * grid_y[k][j]
            line.append(entry)
        output.append(line)
    return output

def mat_trace(grid):
    running = 0
    for i in range(min(len(grid), len(grid[0]))):
        running += grid[i][i]
    return running

def determinant_2x2(grid):
    if len(grid) != 2 or len(grid[0]) != 2:
        return None
    return grid[0][0] * grid[1][1] - grid[0][1] * grid[1][0]

def product_report(grid_x, grid_y):
    result = mat_multiply(grid_x, grid_y)
    if result is None:
        print("Incompatible dimensions for multiplication.")
        return None
    trace = mat_trace(result)
    det_x = determinant_2x2(grid_x)
    det_y = determinant_2x2(grid_y)
    print(f"Grid X          : {grid_x}")
    print(f"Grid Y          : {grid_y}")
    print(f"Product X x Y   :")
    for line in result:
        print(f"  {line}")
    print(f"Trace of result : {trace}")
    if det_x is not None:
        print(f"Det(X)          : {det_x}")
    if det_y is not None:
        print(f"Det(Y)          : {det_y}")
    grand_total = 0
    for line in result:
        for val in line:
            grand_total += val
    print(f"Sum of result   : {grand_total}")
    return result

product_report([[1, 2], [3, 4]], [[5, 6], [7, 8]])
