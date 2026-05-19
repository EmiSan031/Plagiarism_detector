def rotate_table(table):
    converted = []
    for col in range(len(table[0])):
        line = []
        for row_index in range(len(table)):
            line.append(table[row_index][col])
        converted.append(line)
    return converted

def table_total(table):
    grand_total = 0
    for line in table:
        for cell in line:
            grand_total += cell
    return grand_total

def display_table(table, caption):
    print(f"{caption}:")
    for line in table:
        print(f"  {line}")

def rotation_report(table):
    num_rows = len(table)
    num_cols = len(table[0])
    rotated = rotate_table(table)
    display_table(table, "Input table")
    print(f"Input dimensions: {num_rows} rows x {num_cols} columns")
    display_table(rotated, "Rotated table")
    print(f"Rotated dimensions: {num_cols} rows x {num_rows} columns")
    input_total = table_total(table)
    rotated_total = table_total(rotated)
    print(f"Input total     : {input_total}")
    print(f"Rotated total   : {rotated_total}")
    print(f"Totals match    : {input_total == rotated_total}")

rotation_report([[7, 8, 9], [10, 11, 12]])
