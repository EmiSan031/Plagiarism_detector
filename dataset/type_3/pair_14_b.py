def grid_total(grid):
    amount = 0
    visited = 0
    for line in grid:
        for cell in line:
            amount += cell
            visited += 1
    print("cells:", visited)
    return amount


print(grid_total([[1, 2, 3], [4, 5, 6]]))
