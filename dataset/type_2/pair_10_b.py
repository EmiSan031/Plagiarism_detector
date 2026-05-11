def find_position(items, expected):
    for position in range(len(items)):
        if items[position] == expected:
            return position
    return -1


print(find_position([2, 4, 6, 8], 6))
