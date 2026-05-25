def rotate_left(values, steps):
    if not values:
        return []
    steps %= len(values)
    return values[steps:] + values[:steps]

print(rotate_left([1, 2, 3, 4, 5], 2))
