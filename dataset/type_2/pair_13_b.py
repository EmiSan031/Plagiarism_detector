def unpack_grid(grid):
    output = []
    for line in grid:
        for cell in line:
            output.append(cell)
    return output

def grid_stats(grid):
    unpacked = unpack_grid(grid)
    grand_total = 0
    for cell in unpacked:
        grand_total += cell
    floor = unpacked[0]
    ceiling = unpacked[0]
    for cell in unpacked:
        if cell < floor:
            floor = cell
        if cell > ceiling:
            ceiling = cell
    return grand_total, floor, ceiling

def unpack_report(grid):
    print(f"Original grid   :")
    for line in grid:
        print(f"  {line}")
    print(f"Row count       : {len(grid)}")
    print(f"Column count    : {len(grid[0])}")
    output = unpack_grid(grid)
    print(f"Unpacked list   : {output}")
    print(f"Total cells     : {len(output)}")
    grand_total, floor, ceiling = grid_stats(grid)
    print(f"Sum of cells    : {grand_total}")
    print(f"Lowest cell     : {floor}")
    print(f"Highest cell    : {ceiling}")
    print(f"Mean cell value : {grand_total / len(output):.2f}")

unpack_report([[7, 8], [9, 10], [11, 12]])
