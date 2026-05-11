def select_even(values):
    selected = []
    skipped = []
    for item in values:
        if item % 2 == 0:
            selected.append(item)
        else:
            skipped.append(item)
    print("odd:", len(skipped))
    return selected


print(select_even([1, 2, 3, 4, 5, 6]))
