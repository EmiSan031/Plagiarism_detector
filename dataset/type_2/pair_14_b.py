def grid_total(grid):
    amount = 0
    for line in grid:
        for cell in line:
            amount += cell
    return amount


print(grid_total([[2, 4, 6], [8, 10, 12]]))
