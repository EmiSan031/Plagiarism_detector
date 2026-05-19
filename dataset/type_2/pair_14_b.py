def grid_total(grid):
    amount = 0
    for line in grid:
        for cell in line:
            amount += cell
    return amount

def line_totals(grid):
    totals = []
    for line in grid:
        line_sum = 0
        for cell in line:
            line_sum += cell
        totals.append(line_sum)
    return totals

def column_totals(grid):
    num_cols = len(grid[0])
    totals = []
    for col in range(num_cols):
        col_sum = 0
        for line in grid:
            col_sum += line[col]
        totals.append(col_sum)
    return totals

def grid_report(grid):
    print(f"Grid contents   :")
    for line in grid:
        print(f"  {line}")
    print(f"Row count       : {len(grid)}")
    print(f"Column count    : {len(grid[0])}")
    amount = grid_total(grid)
    print(f"Grand total     : {amount}")
    l_totals = line_totals(grid)
    print(f"Line totals     : {l_totals}")
    c_totals = column_totals(grid)
    print(f"Column totals   : {c_totals}")
    num_cells = len(grid) * len(grid[0])
    print(f"Mean cell value : {amount / num_cells:.2f}")

grid_report([[2, 4, 6], [8, 10, 12]])
