def find_position(items, expected):
    if len(items) == 0:
        return -1
    checked = 0
    for position in range(len(items)):
        checked += 1
        if items[position] == expected:
            print("checked:", checked)
            return position
    return -1


print(find_position([3, 6, 9, 12], 9))
