def rotate_table(table):
    if not table:
        return []
    converted = []
    width = len(table[0])
    for col in range(width):
        line = []
        for row_index in range(len(table)):
            line.append(table[row_index][col])
        converted.append(line)
    print("columns:", width)
    return converted


print(rotate_table([[1, 2, 3], [4, 5, 6]]))
