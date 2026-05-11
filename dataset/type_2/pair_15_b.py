def select_even(values):
    selected = []
    for item in values:
        if item % 2 == 0:
            selected.append(item)
    return selected


print(select_even([10, 11, 12, 13, 14, 15]))
