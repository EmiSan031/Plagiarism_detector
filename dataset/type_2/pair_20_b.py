def rotate_table(table):
    converted = []
    for col in range(len(table[0])):
        line = []
        for row_index in range(len(table)):
            line.append(table[row_index][col])
        converted.append(line)
    return converted


print(rotate_table([[7, 8, 9], [10, 11, 12]]))
