def unpack_grid(grid):
    output = []
    for line in grid:
        for cell in line:
            output.append(cell)
    return output


print(unpack_grid([[7, 8], [9, 10], [11, 12]]))
