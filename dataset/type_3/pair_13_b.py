def unpack_grid(grid):
    output = []
    row_count = 0
    for line in grid:
        row_count += 1
        for cell in line:
            output.append(cell)
    print("rows:", row_count)
    return output


print(unpack_grid([[1, 2], [3, 4], [5, 6]]))
