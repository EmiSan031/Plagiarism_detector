def build_series(size):
    if size <= 0:
        return []
    values = []
    first = 0
    second = 1
    for _ in range(size):
        values.append(first)
        first, second = second, first + second
    last_value = values[-1]
    print("last:", last_value)
    return values


print(build_series(8))
